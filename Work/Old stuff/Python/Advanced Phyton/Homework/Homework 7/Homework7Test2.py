import unittest
from Homework7 import checkwordlength


class TestWordlength(unittest.TestCase):
    def test_wordlength(self):
       result = checkwordlength("This is a sample text with some words")
       expected_result = ['sample', 'words']
       self.assertEqual(result, expected_result)
