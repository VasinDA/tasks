class Convertor:
    def __init__(self):
       self.units_dict = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 
       6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
       self.tens_dict ={10: 'X', 20: 'XX', 30: 'XXX'}

    def convertRomansToArabic(self, num):
        if not isinstance(num, int):
            raise 'Not digit'
        if num == 0:
            return ''