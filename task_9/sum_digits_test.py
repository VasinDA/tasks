import unittest
from sum_digits import Sumdigits

class TestSumDigits(unittest.TestCase):
    def test_get_sum_digits(self):
        test_dict = {0: 0, 1: 1, 10: 1, 22: 4, 100: 1, 1200230002: 10, 'a': 'Not digit'}
        test_odject = Sumdigits()
        for key in test_dict:
            self.assertEqual(test_odject.getSumdigits(key), test_dict[key])

unittest.main()

