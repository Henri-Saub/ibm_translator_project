# IMPORT DEPS
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from logging import getLogger, DEBUG

logger = getLogger('ibm-translator-project')
logger.setLevel(DEBUG)


# AUTHENTICATE
apikey = 'l28JkJlJCJeRdDtPaJcAttI8uIrkqofZxr7VNhAU66FZ'
url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/63ce5f51-902a-4b00-9086-4a3d44387f0a'

# SETUP SERVICES
authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(url)


# ENGLISH TO FRENCH TRANSLATION FUNCTION
def english_to_french(text):
    lt.set_service_url(url)
    translate_en_fr = lt.translate(text=text, model_id='en-fr').get_result()['translations'][0]['translation']
    logger.debug(f"input test: {text}, output text: {translate_en_fr}")
    return translate_en_fr


# ENGLISH TO GERMAN TRANSLATION FUNCTION
def english_to_german(text):
    lt.set_service_url(url)
    translate_en_de = lt.translate(text=text, model_id='en-de').get_result()['translations'][0]['translation']
    logger.debug(f"input test: {text}, output text: {translate_en_de}")
    return translate_en_de
