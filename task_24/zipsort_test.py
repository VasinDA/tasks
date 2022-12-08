import unittest
from zipsort import zipSort

class ZipSortTest(unittest.TestCase):
    def setUp(self):
        self.test_arr1 = [1,2,4]
        self.test_arr2 = [3,5]
        self.test_arr3 = []
        
    def zipsort_test_1(self):
        epxpected_result_1 = [1,2,3,4,5]
        self.assertEqual(zipSort(self.test_arr1, self.test_arr2), epxpected_result_1)
        
    def zipsort_test_2(self):
        epxpected_result_2 = [3,5]
        self.assertEqual(zipSort(self.test_arr2, self.test_arr3), epxpected_result_2)
        
    def zipsort_test_3(self):
        epxpected_result_3 = []
        self.assertEqual(zipSort(self.test_arr3, self.test_arr3), epxpected_result_3)


unittest.main()