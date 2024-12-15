import unittest
from lab5.Task1.src.task1 import is_min_heap


class TestCase(unittest.TestCase):
    def test_with_data_task(self):
        self.assertEqual(is_min_heap([1, 0, 1, 2, 0]), "NO")
        self.assertEqual(is_min_heap([1, 3, 2, 5, 4]), "YES")

    def test_with_other_data(self):
        self.assertEqual(is_min_heap([2, 4, 5, 6, 7, 8]), "YES")
        self.assertEqual(is_min_heap([1, 1, 1, 1, 1]), "YES")
        self.assertEqual(is_min_heap([3, 5, 4, 6]), "YES")
        self.assertEqual(is_min_heap([10, 7, 5, 12]), "NO")


if __name__ == '__main__':
    unittest.main()
