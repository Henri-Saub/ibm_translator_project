# IMPORT UNITTEST
import unittest

from ibm_cloud_sdk_core import ApiException
from src.translator import english_to_french, english_to_german


class TestEnglishToFrench(unittest.TestCase):
    def test_hello(self):
        self.assertEqual('Bonjour', english_to_french('hello'))

    def test_verb(self):
        self.assertEqual('à manger', english_to_french('to eat'))

    def test_dummy(self):
        self.assertNotEqual('il fait beau', english_to_french('how are you'))

    def test_empty(self):
        with self.assertRaises(ApiException):
            english_to_french('')


class TestEnglishToGerman(unittest.TestCase):

    def test_hello(self):
        self.assertEqual('Hallo', english_to_german('hello'))

    def test_verb(self):
        self.assertEqual('zu essen', english_to_german('to eat'))

    def test_dummy(self):
        self.assertNotEqual('es ist sonnig', english_to_german('how are you'))

    def test_empty(self):
        with self.assertRaises(ApiException):
            english_to_german('')


if __name__ == '_main_':
    unittest.main()
