import unittest
from palindrome import palinDrome

class TestPalinDrome(unittest.TestCase):
    def test_palindrome(self):
        # TODO: to check with "133a123" -> True
        test_dict = {'арозаупаланалапуазора': True, 'арозаупаланалапуазорА': True, 'Ка1бак': True, 'a': True, '': False,
        '1111111': False, 'a124a': True, '4': False}
        for key in test_dict:
            self.assertEqual(palinDrome(key), test_dict[key])

unittest.main()
