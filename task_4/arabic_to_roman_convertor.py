class Convertor:
    def __init__(self):
       self.dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 
       500: 'D', 1000: 'M'}
             
    def convertArabicToRomans(self, num):
        rom_digit = ''
        if not isinstance(num, int):
            return 'Not digit'
        if num == 0:
            return ''
        str_num = str(num)
        str_num = str_num[::-1]
        len_num = len(str_num)
        flag = 1
        for digit in str_num:
            digit = int(digit) 
            if digit == 0:
                rom_digit = rom_digit
            elif digit in [1, 2, 3]:
                rom_digit = self.dict[flag] * digit + rom_digit
            elif digit == 4:
                rom_digit = self.dict[flag] + self.dict[flag * 5] + rom_digit
            elif digit in [5, 6, 7, 8]:
               rom_digit = self.dict[flag * 5] + self.dict[flag] * (digit - 5) + rom_digit
            elif digit == 9:
               rom_digit = self.dict[flag] + self.dict[flag * 10] + rom_digit
            flag *= 10
        return rom_digit
        