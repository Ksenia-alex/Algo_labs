import unittest
from lab7.Task1.src.task1 import min_coins


class TestCase(unittest.TestCase):
    def test_with_data_task(self):
        self.assertEqual(min_coins(2, [1, 3, 4]), 2)
        self.assertEqual(min_coins(34, [1, 3, 4]), 9)

    def test_with_other_data(self):
        self.assertEqual(min_coins(12, [1, 3, 4, 6, 7, 8, 23]), 2)
        self.assertEqual(min_coins(13, [1, 3, 5, 7, 9, 2, 3, 4, 4]), 2)
        self.assertEqual(min_coins(123, [1, 3, 4]), 31)
        self.assertEqual(min_coins(3, [1]), 3)
        self.assertEqual(min_coins(1, [1]), 1)


if __name__ == '__main__':
    unittest.main()
