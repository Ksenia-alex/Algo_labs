import unittest
from lab7.Task6.src.task6 import max_increasing_subsequence


class TestCase(unittest.TestCase):
    def test_with_data_task(self):
        self.assertEqual(max_increasing_subsequence([3, 29, 5, 5, 28, 6]), (3, [3, 5, 28]))

    def test_with_other_data(self):
        self.assertEqual(max_increasing_subsequence([0, 1, 2, 3, 0, 1]), (4, [0, 1, 2, 3]))
        self.assertEqual(max_increasing_subsequence([3, 6, 7, 9, 1, 3, 4, 5]), (4, [3, 6, 7, 9]))
        self.assertEqual(max_increasing_subsequence([5, 6, 7, 82, 3, 4, 1]), (4, [5, 6, 7, 82]))
        self.assertEqual(max_increasing_subsequence([0, 0, 0, 0, 0]), (1, [0]))
        self.assertEqual(max_increasing_subsequence([1, 1, 2, 0]), (2, [1, 2]))
        self.assertEqual(max_increasing_subsequence([]), 0)


if __name__ == '__main__':
    unittest.main()
