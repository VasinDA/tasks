import unittest
from numbers_to_words import TextByNumberConvertor

class TestTextByNumberConvertor(unittest.TestCase):
    def test_get_text_by_number_en(self):
        test_dict = {0: 'zero', 5: 'five', 10: 'ten', 15: 'fifteen', 20: 'twenty', 25: 'twenty five'}
        test_text = TextByNumberConvertor()
        for key in test_dict:
            self.assertEqual(test_text.getTextByNumber(key), test_dict[key])
    
    def test_get_text_by_number_ua(self):
        test_dict = {0: 'нуль', 5: "п'ять", 10: 'десять', 15: "п'ятнадцять", 20: 'двадцять', 25: "двадцять п'ять"}
        lang = 'ua'
        test_text = TextByNumberConvertor()
        for key in test_dict:
            self.assertEqual(test_text.getTextByNumber(key, lang = lang), test_dict[key])

    def test_get_text_by_number_ru(self):
        test_dict = {0: 'ноль', 5: "пять", 10: 'десять', 15: "пятнадцать", 20: 'двадцать', 25: "двадцать пять"}
        lang = 'ru'
        test_text = TextByNumberConvertor()
        for key in test_dict:
            self.assertEqual(test_text.getTextByNumber(key, lang = lang), test_dict[key])


unittest.main()
        