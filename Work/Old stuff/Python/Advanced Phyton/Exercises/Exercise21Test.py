import unittest
from Exercise21 import subtraction

class TestSubtraction(unittest.TestCase):

    def test_subtraction_successfully1(self):
        result = subtraction(10,5)
        expected_result = 5
        self.assertEqual(result,expected_result)
    def test_subtraction_successfully2(self):
        result = subtraction(5,10)
        expected_result = -5
        self.assertEqual(result,expected_result)
    def test_subtraction_successfully3(self):
        result = subtraction(-8, -7)
        expected_result = -1
        self.assertEqual(result, expected_result)
    def test_subtraction_successfully4(self):
        result = subtraction(6,-7)
        expected_result = 13
        self.assertEqual(result,expected_result)
    def test_subtraction_successfully5(self):
        result = subtraction(-13,8)
        expected_result = -21
        self.assertEqual(result,expected_result)
