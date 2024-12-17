import unittest
from lab7.Task5.src.task5 import max_increasing_subsequence


class TestCase(unittest.TestCase):
    def test_with_data_task(self):
        self.assertEqual(max_increasing_subsequence([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]), 3)
        self.assertEqual(max_increasing_subsequence([1, 2, 3], [2, 1, 3], [1, 3, 5]), 2)

    def test_with_other_data(self):
        self.assertEqual(max_increasing_subsequence([1, 2, 3, 4, 5], [], [1]), 0)
        self.assertEqual(max_increasing_subsequence([3, 7, 1, 9, 12], [4, 6, 2, 9, 3, 4, 12], [2, 3, 12, 5, 7]), 2)
        self.assertEqual(max_increasing_subsequence([1, 0, 2, 9, 9, 9], [1, 7, 3, 0, 3, 2], [1]), 1)
        self.assertEqual(max_increasing_subsequence([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]), 5)
        self.assertEqual(max_increasing_subsequence([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]), 4)


if __name__ == '__main__':
    unittest.main()
