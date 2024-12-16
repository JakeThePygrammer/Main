import unittest
from Exercise22 import palindromechecker

class TestPalindromeChecker(unittest.TestCase):

    def test_palindromechecker_successfully1(self):
        result = palindromechecker("ana")
        expected_result = True
        self.assertEqual(result,expected_result)
    def test_palindromechecker_unsuccessfully1(self):
        result = palindromechecker("phyton")
        expected_result = False
        self.assertEqual(result,expected_result)
