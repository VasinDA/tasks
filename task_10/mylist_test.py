from cgi import test
import unittest
from mylist import Mylist

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
        test_data = 1
        self.mylist = self.mylist.remove(test_data)
        self.assertEqual(self.mylist.__eq__(test_mylist), expected_result)
    
    def test_replace_includes(self):
        test_old_value = 2
        test_new_value = 8
        test_hit_counter = 1
        test_includes_value = 8
        test_includes_value_wrong = 10
        expected_result_includes = True
        expected_result_includes_wrong = False
        self.assertEqual(self.mylist.replace(test_old_value, test_new_value), test_hit_counter)
        self.assertEqual(self.mylist.includes(test_includes_value), expected_result_includes)
        self.assertEqual(self.mylist.includes(test_includes_value_wrong), expected_result_includes_wrong)



unittest.main()