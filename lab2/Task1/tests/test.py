import unittest
from lab2.task1.src.task1 import merge_sort


class TestCase(unittest.TestCase):
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(merge_sort(arr), [1, 2, 3, 4, 5])
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(merge_sort(arr), [1, 2, 3, 4, 5])
        arr = [12, 11, 13, 5, 6, 7]
        self.assertEqual(merge_sort(arr), [5, 6, 7, 11, 12, 13])
        arr = [3, 1, 2, 3, 4, 4, 2]
        self.assertEqual(merge_sort(arr), [1, 2, 2, 3, 3, 4, 4])
        arr = [42]
        self.assertEqual(merge_sort(arr), [42])
        arr = []
        self.assertEqual(merge_sort(arr), [])
        arr = [100000, 5000, 1000000, 50000]
        self.assertEqual(merge_sort(arr), [5000, 50000, 100000, 1000000])
        arr = [-5, -3, -4, -1, -2]
        self.assertEqual(merge_sort(arr), [-5, -4, -3, -2, -1])
        arr = [10, -5, 3, 7, -2, 5]
        self.assertEqual(merge_sort(arr), [-5, -2, 3, 5, 7, 10])


if __name__ == '__main__':
    unittest.main()
