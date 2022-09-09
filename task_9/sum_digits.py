class Sumdigits:
    def getSumdigits(self, digit):
        if not isinstance(digit, int):
            return 'Not digit'
        str_digit = str(digit)
        list_digits = [int(digit) for digit in str_digit]
        return sum(list_digits)
