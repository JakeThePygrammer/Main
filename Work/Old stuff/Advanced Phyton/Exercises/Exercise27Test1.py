import unittest
from Exercise27 import librarysystem

class TestLibrarySystem(unittest.TestCase):

    def test_librarysystem_1(self):
        result = librarysystem(500,False,700)
        expectedresult = True
        self.assertEqual(result, expectedresult)

    def test_librarysystem_2(self):
        result = librarysystem(500,True,700)
        expectedresult = False
        self.assertEqual(result, expectedresult)

    def test_librarysystem_3(self):
        result = librarysystem(500,False,300)
        expectedresult = 403
        self.assertEqual(result, expectedresult)

    def test_librarysystem_4(self):
        result = librarysystem(500,True,700)
        expectedresult = False
        self.assertEqual(result, expectedresult)
    def test_librarysystem_5(self):
        result = librarysystem(500,False,500)
        expectedresult = True
        self.assertEqual(result, expectedresult)


