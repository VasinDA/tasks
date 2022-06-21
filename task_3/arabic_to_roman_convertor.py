class Convertor:
    def __init__(self):
       self.units_dict = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 
       6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', }
       self.tens_dict = {1: 'X', 2: 'XX', 3: 'XXX'}

    def convertArabicToRomans(self, num):
        if not isinstance(num, int):
            raise 'Not digit'
        if num == 0:
            return ''
        units = num % 10
        tens = num // 10
        if tens == 0:
            return self.units_dict[units]
        if units == 0:
            return self.tens_dict[tens]
        return '{}{}'.format(self.tens_dict[tens], self.units_dict[units])