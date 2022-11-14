from cgi import test
import unittest
from mylist import Mylist

class TestMylist(unittest.TestCase):
    def setUp(self):
        self.mylist = Mylist(1,3,2,4)
        self.sorted_up_mylist = Mylist(1,2,4)
        self.sorted_down_mylist = Mylist(4,2,1)
        self.unsorted_mylist = Mylist(1,4,2)
        self.test_dict = {2: 2, 0: -1}
        self.remove_test_data = 1
        self.test_old_value = 2
        self.test_new_value = 8
        self.test_wrong_value = 10
        self.test_value = 4
    
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
        for data in self.test_dict:
            self.assertEqual(self.mylist.find(data), self.test_dict[data])

    def test_remove(self):
        expected_result = True
        expected_result_wrong_index = True
        wrong_index_remove = 4
        test_mylist = Mylist(1,2,4)
        self.mylist = self.mylist.remove(wrong_index_remove)
        self.assertEqual(self.mylist.__eq__(self.mylist), expected_result_wrong_index)
        self.mylist = self.mylist.remove(self.remove_test_data)
        self.assertEqual(self.mylist.__eq__(test_mylist), expected_result)
    
    def test_replace_includes(self):
        test_hint_counter = 1
        test_wrong_replace_value_counter = 0
        self.assertEqual(self.mylist.replace(self.test_old_value, self.test_new_value), test_hint_counter)
        self.assertEqual(self.mylist.replace(self.test_wrong_value, self.test_new_value), test_wrong_replace_value_counter)
        
    def test_includes(self):
        expected_result_includes = True
        expected_result_includes_wrong = False
        self.assertEqual(self.mylist.includes(self.test_value), expected_result_includes)
        self.assertEqual(self.mylist.includes(self.test_wrong_value), expected_result_includes_wrong)
    
    def test_is_sorted(self):
        expected_result_for_sorted_mylist = True
        expected_result_for_unsorted_mylist = False
        self.assertEqual(self.sorted_up_mylist.isSorted(), expected_result_for_sorted_mylist)
        self.assertEqual(self.unsorted_mylist.isSorted(), expected_result_for_unsorted_mylist)
    
    def test_sort_direction(self):
        expected_result_for_sorted_up_mylist = 1
        expected_result_for_sorted_down_mylist = -1
        expected_result_for_unsorted_mylist = 0
        self.assertEqual(self.sorted_up_mylist.sortDirection(),  expected_result_for_sorted_up_mylist)
        self.assertEqual(self.sorted_down_mylist.sortDirection(),  expected_result_for_sorted_down_mylist)
        self.assertEqual(self.unsorted_mylist.sortDirection(), expected_result_for_unsorted_mylist)
    
    def test_count(self):
        expected_result_with_value = 1
        expected_result_without_value = 4
        expected_result_wrong_value = 0
        self.assertEqual(self.mylist.count(self.test_value), expected_result_with_value)
        self.assertEqual(self.mylist.count(self.test_wrong_value), expected_result_wrong_value)
        self.assertEqual(self.mylist.count(), expected_result_without_value)

    def test_append(self):
        test_value = 5
        test_list = [1,3,2,4,5]
        self.assertEqual(self.mylist.append(test_value), test_list)
    
    def test_insert(self):
        test_index_value = 2
        old_value = 2
        new_value = 7
        wrong_index = -1
        expected_result = None
        self.assertEqual(self.mylist.find(old_value), test_index_value)
        test_list = self.mylist.insert(test_index_value, new_value)
        self.assertEqual(test_list[test_index_value], new_value)
        self.assertEqual(self.mylist.insert(wrong_index, new_value), expected_result)
    
    def test_concat(self):
        test_mylist = Mylist(1,2,3)
        concat_list = Mylist(3,2,1)
        empty_concat_list = Mylist()
        expected_result = [1,2,3,3,2,1]
        expected_result_empty_list = [1,2,3]
        self.assertEqual(test_mylist.concat(empty_concat_list), expected_result_empty_list)
        self.assertEqual(test_mylist.concat(concat_list), expected_result)
    
    def test_clear(self):
        test_len = 0
        expected_result = []
        self.assertNotEqual(self.mylist.lenList(), test_len)
        self.assertEqual(self.mylist.clear(), expected_result)
    
    def test_sort(self):
        direction_up = 1
        direction_down = -1
        direction_zero = 0
        expected_result_up = [1,2,4]
        expected_result_down = [4,2,1]
        expected_result_zero = [1,4,2]
        self.assertEqual(self.sorted_up_mylist.sort(direction_up), expected_result_up)
        self.assertEqual(self.unsorted_mylist.sort(direction_zero), expected_result_zero)
        self.assertEqual(self.unsorted_mylist.sort(direction_up), expected_result_up)
        self.assertEqual(self.unsorted_mylist.sort(direction_down), expected_result_down)

    def test_empty_list(self):
        empty_mylist = Mylist()
        append_value = 1
        sort_direction = 1
        expected_result_append = [1]
        expected_result_for_min_max_avg_remove_sortdirection = None
        expected_result_for_find_replace = -1
        expected_result_for_includes_issorted = False
        expected_result_for_count = 0
        expected_result_sort =[]
        self.assertEqual(empty_mylist.min(), expected_result_for_min_max_avg_remove_sortdirection)
        self.assertEqual(empty_mylist.max(), expected_result_for_min_max_avg_remove_sortdirection)
        self.assertEqual(empty_mylist.avg(), expected_result_for_min_max_avg_remove_sortdirection)
        self.assertEqual(empty_mylist.find(self.test_dict), expected_result_for_find_replace)
        self.assertEqual(empty_mylist.remove(self.remove_test_data), expected_result_for_min_max_avg_remove_sortdirection)
        self.assertEqual(empty_mylist.includes(self.test_value), expected_result_for_includes_issorted)
        self.assertEqual(empty_mylist.replace(self.test_old_value, self.test_new_value), expected_result_for_find_replace)
        self.assertEqual(empty_mylist.sortDirection(), expected_result_for_min_max_avg_remove_sortdirection)
        self.assertEqual(empty_mylist.isSorted(), expected_result_for_includes_issorted)
        self.assertEqual(empty_mylist.count(), expected_result_for_count)
        self.assertEqual(empty_mylist.sort(sort_direction), expected_result_sort)
        self.assertEqual(empty_mylist.append(append_value), expected_result_append)


unittest.main()