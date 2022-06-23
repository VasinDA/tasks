from cgi import test
import unittest
from arabic_to_roman_convertor import Convertor

class TestConvertor(unittest.TestCase):
    def test_convet_arabic_to_romans(self):
        arabic_to_roman = Convertor()
        test_dict = {'qw': 'Not digit', 0: '', 40: 'XL', 44: 'XLIV', 52: 'LII', 74: 'LXXIV', 
        96: 'XCVI', 99: 'XCIX', 409: 'CDIX', 999 : 'CMXCIX'}
        for key in test_dict:
            self.assertEqual(arabic_to_roman.convertArabicToRomans(key), test_dict[key])

unittest.main()