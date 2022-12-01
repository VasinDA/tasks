import unittest
from zipsort import zipSort

class ZipSortTest(unittest.TestCase):
    def zipsort_test(self):
        test_arr1 = [1,2,4]
        test_arr2 = [3,5]
        epxpected_result_1 = [1,2,3,4,5]
        test_arr3 = []
        epxpected_result_2 = [3,5]
        epxpected_result_3 = []
        self.assertEqual(zipSort(test_arr1, test_arr2), epxpected_result_1)
        self.assertEqual(zipSort(test_arr2, test_arr3), epxpected_result_2)
        self.assertEqual(zipSort(test_arr3, test_arr3), epxpected_result_3)

unittest.main()