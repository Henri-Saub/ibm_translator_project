"""Translator"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from decouple import config

APIKEY = config('APIKEY')
URL = config('URL')

AUTHENTICATOR = IAMAuthenticator(APIKEY)
LT = LanguageTranslatorV3(version='2018-05-01', authenticator=AUTHENTICATOR)
LT.set_service_url(URL)


def english_to_french(text):
    """translates english to French"""
    LT.set_service_url(URL)
    translate_en_fr = LT.translate(text=text, model_id='en-fr').get_result\
        ()['translations'][0]['translation']
    return translate_en_fr


# ENGLISH TO GERMAN TRANSLATION FUNCTION
def english_to_german(text):
    """translates english to german"""
    LT.set_service_url(URL)
    translate_en_de = LT.translate(text=text, model_id='en-de').get_result\
        ()['translations'][0]['translation']
    return translate_en_de
