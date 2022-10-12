from cgi import test
import unittest
from list import Mylist

class TestMylist(unittest.TestCase):
    def setUp(self):
        self.mylist = Mylist(1,3,2,4)
    
    def test_min(self):
        expected_result = 1
        self.assertEqual(self.mylist.min(), expected_result)

    def test_max(self):
        expected_result = 4
        self.assertEqual(self.mylist.max(), expected_result)
    
    def test_avg(self):
        expected_result = 2.5
        self.assertEqual(self.mylist.avg(), expected_result)
    
    def test_find(self):
        test_dict = {2: 2, 0: -1}
        for data in test_dict:
            self.assertEqual(self.mylist.find(data), test_dict[data])

    def test_remove(self):
        expected_result = True
        test_mylist = Mylist(1,2,4)
        self.assertEqual(self.__eq__(test_mylist), expected_result)
    
    def __eq__(self, other):
        test_data = 1
        self.mylist = self.mylist.remove(test_data)
        if isinstance(other, Mylist):
            return self.mylist.tuple == other.tuple
        return NotImplemented


unittest.main()