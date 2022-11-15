import unittest
from couldbesorted import couldBeSorted

class TestcouldBeSorted(unittest.TestCase):
    def test_couldbesorted(self):
        test_dict = {0: [1,2,4,3], 1: [1,3,2,4], 2: [1,4,2,3], 3: [4,2,3,1], 
            4:[6,2,4,3,1], 5: [6,2,3,4,1], 6:[6,2,3,4,5,1]}
        test_list = [True, True, False, True, False, True, True]
        for index in range(len(test_list)):
            self.assertEqual(couldBeSorted(test_dict[index]), test_list[index])

unittest.main()