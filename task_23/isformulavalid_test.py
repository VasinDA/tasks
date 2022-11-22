import unittest
from isformulavalid import isFormulaValid

class TestIsFormulaValid(unittest.TestCase):
    def test_isformulavalid(self):
        test_dict = {'()': True, '(())': True, '()(': False, '(()(()': False, ')(': False,
        '': True, '(': False, '(()(())())': True, '())(()': False}
        for key in test_dict:
            self.assertEqual(isFormulaValid(key), test_dict[key])

unittest.main()