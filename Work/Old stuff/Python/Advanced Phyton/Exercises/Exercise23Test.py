import unittest
from Exercise23 import textcheck

class TestTextChecker(unittest.TestCase):

    def test_textchecker_successfully1(self):
        result = textcheck("")
        expectedresult = {}
        self.assertEqual(result, expectedresult)
    def test_textchecker_successfully2(self):
        result = textcheck("Fun")
        expectedresult = {"fun" : 1}
        self.assertEqual(result, expectedresult)
    def test_textchecker_successfully3(self):
        result = textcheck("I am fun")
        expectedresult = {"i" : 1, "am" : 1, "fun" : 1}
        self.assertEqual(result, expectedresult)
    def test_textchecker_successfully4(self):
        result = textcheck("i i am fun fun")
        expectedresult = {"i" : 2, "am" : 1, "fun" : 2}
        self.assertEqual(result, expectedresult)
    def test_textchecker_successfully5(self):
        result = textcheck("I AM fun Fun am i right")
        expectedresult = {"i" : 2, "am" : 2, "fun" : 2, "right" : 1}
        self.assertEqual(result, expectedresult)
