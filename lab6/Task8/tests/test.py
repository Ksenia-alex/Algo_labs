import unittest
from lab6.Task8.src.task8 import solve


class TestCase(unittest.TestCase):
    def test_with_data_task(self):
        self.assertEqual(solve(4, 0, 0, 0, 1, 1, 0, 0), (3, 1, 1))

    def test_with_other_data(self):
        self.assertEqual(solve(2, 100, 1, 1, 1, 1, 1, 1), (609, 3, 3))
        self.assertEqual(solve(3, 1, 2, 3, 4, 5, 6, 7), (5404, 20, 24))
        self.assertEqual(solve(1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0))
        self.assertEqual(solve(5, 999999999999, 1000, 500000000000, 2, 3, 1, 999), (223000000324555, 5, 500000004995))
        self.assertEqual(solve(6, 10, 1, 2, 3, 4, 5, 6), (206722298, 31, 38))


if __name__ == '__main__':
    unittest.main()
