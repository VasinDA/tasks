class TextByNumberConvertor:
    def __init__(self):
        self.dict_units_en = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero', 10: 'ten', 11: 'eleven', 
        12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 
        18: 'eightteen', 19: 'nineteen'}
        self.dict_tens_en = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5:'fifty', 6: 'sixty', 
        7: 'seventy', 8: 'eighty', 9: 'ninety'}
        self.dict_units_ua = {1: 'один', 2: 'два', 3: 'три', 4: 'чотири', 5: "п'ять", 
        6: 'шість', 7: 'сім', 8: 'вісім', 9: "дев'ять", 0: 'нуль', 10: 'десять', 11: 'одинадцять', 12: 'дванадцять', 
        13: 'тринадцять', 14: 'чотирнадцять', 15: "п'ятнадцять", 16: 'шістнадцять', 17: 'сімнадцять', 18: 'вісімнадцять', 19: "дев'ятнадцять"}
        self.dict_tens_ua = {2: 'двадцять', 3: 'тридцять', 4: 'сорок', 5: "п'ятдесят", 6: 'шістдесят', 7: 'сімдесят', 
        8: 'вісімдесят', 9:  "дев'яносто"}
        self.dict_units_ru = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: "пять", 
        6: 'шесть', 7: 'семь', 8: 'восемь', 9: "девять", 0: 'ноль', 10: 'десять', 11: 'одинадцать', 12: 'двенадцать', 
        13: 'тринадцять', 14: 'четырнадцать', 15: "пятнадцать", 16: 'шестнадцать', 17: 'семьнадцать', 18: 'восемнадцать', 19: "дев'ятнадцять"}
        self.dict_tens_ru = {2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: "пятдесят", 6: 'шестьдесят', 7: 'семьдесят', 
        8: 'восемдесят', 9:  "девяносто"}

        
    def getTextByNumber(self, digit, lang ='en'):
        lang = lang
        digit = digit
        match lang:
            case 'en':
                dict_units = self.dict_units_en
                dict_tens = self.dict_tens_en
            case 'ua':
                dict_units = self.dict_units_ua
                dict_tens = self.dict_tens_ua
            case 'ru':
                dict_units = self.dict_units_ru
                dict_tens = self.dict_tens_ru
        if 0 <= digit < 20:
            return dict_units[digit]
        if digit % 10 == 0:
            return dict_tens[digit//10]
        return f'{dict_tens[digit//10]} {dict_units[digit%10]}'