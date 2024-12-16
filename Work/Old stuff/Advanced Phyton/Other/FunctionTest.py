import unittest
from FunctionName import presmetaj_zbir
class TestPresmetajZbir(unittest.TestCase):

    def test_presmetaj_zbir_uspeshno(self):
        rezultat_od_funk = presmetaj_zbir(6,7)
        ochekuvan_rezultat = 13
        self.assertEqual(rezultat_od_funk,ochekuvan_rezultat)
