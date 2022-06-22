import unittest
from arabic_to_roman_convertor import Convertor

class TestConvertor(unittest.TestCase):
    def test_convet_arabic_to_romans(self):
        arabic_to_roman = Convertor()
        test_dict = {'qw': 'Not digit', 0: '', 1: 'I', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 9: 'IX', 11: 'XI', 14: 'XIV', 24: 'XXIV', 29: 'XXIX', 34: 'XXXIV'}
        for key in test_dict:
            self.assertEqual(arabic_to_roman.convertArabicToRomans(key), test_dict[key])

unittest.main()