import unittest
from datetime import datetime

from Exercise28 import timefunction

class TestForTimeFunction(unittest.TestCase):

    def test_timefunction_1(self):
        result = timefunction("2012-11-3","2024-11-16")
        expectedresult = datetime.strptime("2024-11-16", "%Y-%m-%d")
        self.assertEqual(result, expectedresult)
    def test_timefunction_2(self):
        result = timefunction("2026-9-3","2012-11-16")
        expectedresult = datetime.strptime("2026-9-3", "%Y-%m-%d")
        self.assertEqual(result, expectedresult)
    def test_timefunction_3(self):
        result = timefunction("2012-11-3","2012-11-3")
        expectedresult = "The dates are equal"
        self.assertEqual(result, expectedresult)
    def test_timefunction_4(self):
        result = timefunction("2012-11-3","2012-11-4")
        expectedresult = datetime.strptime("2012-11-4", "%Y-%m-%d")
        self.assertEqual(result, expectedresult)