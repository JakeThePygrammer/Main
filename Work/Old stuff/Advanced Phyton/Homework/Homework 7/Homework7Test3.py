import unittest
from Homework7 import squarednumberinput


class TestSquared(unittest.TestCase):
    def test_squared(self):
       result = squarednumberinput([1, 2, 3, 4, 5])
       expected_result = [1, 4, 9, 16, 25]
       self.assertEqual(result, expected_result)
