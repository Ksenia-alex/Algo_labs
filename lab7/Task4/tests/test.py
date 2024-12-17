import unittest
from lab7.Task4.src.task4 import max_increasing_subsequence


class MyTestCase(unittest.TestCase):
    def test_with_data_task(self):
        self.assertEqual(max_increasing_subsequence([2, 7, 5], [2, 5]), 2)
        self.assertEqual(max_increasing_subsequence([7], [1, 2, 3, 4]), 0)
        self.assertEqual(max_increasing_subsequence([2, 7, 8, 3], [5, 2, 8, 7]), 2)

    def test_with_other_data(self):
        self.assertEqual(max_increasing_subsequence([1, 2, 3, 4, 5], []), 0)
        self.assertEqual(max_increasing_subsequence([3, 7, 1, 9, 12], [4, 6, 2, 9, 3, 4, 12]), 2)
        self.assertEqual(max_increasing_subsequence([1, 0, 2, 9, 9, 9], [1, 7, 3, 0, 3, 2]), 3)
        self.assertEqual(max_increasing_subsequence([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]), 5)
        self.assertEqual(max_increasing_subsequence([1, 2, 3, 4], [1, 2, 3, 4]), 4)

if __name__ == '__main__':
    unittest.main()
