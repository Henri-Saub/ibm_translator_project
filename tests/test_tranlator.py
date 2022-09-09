"""unitest translator"""
import unittest

from ibm_cloud_sdk_core import ApiException
from src.translator import english_to_french, english_to_german


class TestEnglishToFrench(unittest.TestCase):
    """test english to French translation"""
    def test_hello(self):
        """test hello word"""
        self.assertEqual('Bonjour', english_to_french('hello'))

    def test_verb(self):
        """test a verb"""
        self.assertEqual('à manger', english_to_french('to eat'))

    def test_dummy(self):
        """test if not translate whatever"""
        self.assertNotEqual('il fait beau', english_to_french('how are you'))

    def test_empty(self):
        """test if api error for bad text"""
        with self.assertRaises(ApiException):
            english_to_french('')


class TestEnglishToGerman(unittest.TestCase):
    """test english to german translation"""

    def test_hello(self):
        """test hello word"""
        self.assertEqual('Hallo', english_to_german('hello'))

    def test_verb(self):
        """test a verb"""
        self.assertEqual('zu essen', english_to_german('to eat'))

    def test_dummy(self):
        """test if not translate whatever"""
        self.assertNotEqual('es ist sonnig', english_to_german('how are you'))

    def test_empty(self):
        """test if api error for bad text"""
        with self.assertRaises(ApiException):
            english_to_german('')


if __name__ == '_main_':
    unittest.main()
