import unittest
from Exercise27 import evennumbers

class TestForEvenNumbers(unittest.TestCase):

    def test_evennumbers_1(self):
        result = evennumbers([5,10,15,16,25,38,6,12])
        expectedresult = "New list : [10, 16, 38, 6, 12], removed numbers : [5, 15, 25]"
        self.assertEqual(result, expectedresult)
    def test_evennumbers_2(self):
        result = evennumbers([5,33,13,69,15,25])
        expectedresult = "New list : [], removed numbers : [5, 33, 13, 69, 15, 25]"
        self.assertEqual(result, expectedresult)
    def test_evennumbers_3(self):
        result = evennumbers([4,10,14,16,26,38,6,12])
        expectedresult = "New list : [4, 10, 14, 16, 26, 38, 6, 12], removed numbers : []"
        self.assertEqual(result, expectedresult)
    def test_evennumbers_4(self):
        result = evennumbers([])
        expectedresult = "New list : [], removed numbers : []"
        self.assertEqual(result, expectedresult)
