import unittest
from Exercise24 import analiza_string


class TestAnalizaString(unittest.TestCase):


   def test_samo_soglaski(self):
       rezultat = analiza_string("tsjkl")
       ochekuvan_rezultat = {'soglaski': 5, 'samoglaski': 0, 'cifri': 0, 'karakteri': 0}
       self.assertEqual(rezultat, ochekuvan_rezultat)


   def test_samo_cifri(self):
       rezultat = analiza_string("123")
       ochekuvan_rezultat = {'soglaski': 0, 'samoglaski': 0, 'cifri': 3, 'karakteri': 0}
       self.assertEqual(rezultat, ochekuvan_rezultat)


   def test_samoglaski_i_cifri(self):
       rezultat = analiza_string("aei1")
       ochekuvan_rezultat = {'soglaski': 0, 'samoglaski': 3, 'cifri': 1, 'karakteri': 0}
       self.assertEqual(rezultat, ochekuvan_rezultat)


   def test_karakteri_i_bukvi(self):
       rezultat = analiza_string("as!@#$%^ee")
       ochekuvan_rezultat = {'soglaski': 1, 'samoglaski': 3, 'cifri': 0, 'karakteri': 6}
       self.assertEqual(rezultat, ochekuvan_rezultat)