import unittest
from Homework7 import makenumlist


class TestNumlist(unittest.TestCase):
    def test_numlist(self):
       result = makenumlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
       expected_result = [2, 4, 6, 8, 10]
       self.assertEqual(result, expected_result)
