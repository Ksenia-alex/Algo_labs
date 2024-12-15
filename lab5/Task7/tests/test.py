import unittest
from lab5.Task7.src.task7 import heap_sort


class TestCase(unittest.TestCase):
    def test_array(self):
        arr = [10, 20, 30, 40, 50]
        sorted_arr = heap_sort(arr)
        self.assertEqual(sorted_arr, [10, 20, 30, 40, 50])
        arr = [50, 40, 30, 20, 10]
        sorted_arr = heap_sort(arr)
        self.assertEqual(sorted_arr, [10, 20, 30, 40, 50])
        arr = [12, 11, 13, 5, 6, 7]
        sorted_arr = heap_sort(arr)
        self.assertEqual(sorted_arr, [5, 6, 7, 11, 12, 13])
        arr = [42]
        sorted_arr = heap_sort(arr)
        self.assertEqual(sorted_arr, [42])
        arr = []
        sorted_arr = heap_sort(arr)
        self.assertEqual(sorted_arr, [])


if __name__ == '__main__':
    unittest.main()
