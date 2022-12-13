import unittest
from wordwithoutalfamatch import wordWithOutAlfaMatches

class TestWordWithOutAlfaMatches(unittest.TestCase):
    def test_wordwithoutalfamatches(self):
        test_dict = {'Доброе утро': ['утро'], 'сегодня 19 ноября': ['сегодня'], 
        'как твое здоровье?': ['твое'], 'Сейчас зима?': ['зима'], 'сейчас - осень':[ 'осень'], 
        '': [], 'а': ['а']}
        for key in test_dict:
            self.assertEqual(wordWithOutAlfaMatches(key), test_dict[key])

unittest.main()