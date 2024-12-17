import unittest
from lab3.task1.src.Task1_2 import randomizer_quicksort


class TestCase(unittest.TestCase):
    def test_with_data_task(self):
        arr = [2, 3, 9, 2, 2]
        randomizer_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [2, 2, 2, 3, 9])

    def test_with_other_data(self):
        arr = [1, 2, 3, 4, 5]
        randomizer_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        arr = [5, 4, 3, 2, 1]
        randomizer_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        arr = [12, 11, 13, 5, 6, 7]
        randomizer_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [5, 6, 7, 11, 12, 13])
        arr = [3, 1, 2, 3, 4, 4, 2]
        randomizer_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 2, 3, 3, 4, 4])
        arr = [42]
        randomizer_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [42])
        arr = []
        randomizer_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [])
        arr = [100000, 5000, 1000000, 50000]
        randomizer_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [5000, 50000, 100000, 1000000])
        arr = [-5, -3, -4, -1, -2]
        randomizer_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [-5, -4, -3, -2, -1])
        arr = [10, -5, 3, 7, -2, 5]
        randomizer_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [-5, -2, 3, 5, 7, 10])


if __name__ == '__main__':
    unittest.main()