import unittest
from lab5.Task5.src.task5 import parallel_task_processing


class TestCase(unittest.TestCase):
    def test_with_data_task(self):
        self.assertEqual(parallel_task_processing(2, 5, [1, 2, 3, 4, 5]),
                         [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)])
        self.assertEqual(parallel_task_processing(4, 20,
                                                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
                         [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2),
                          (2, 2), (3, 2), (0, 3), (1, 3), (2, 3), (3, 3), (0, 4), (1, 4), (2, 4), (3, 4)])

    def test_with_other_data(self):
        self.assertEqual(parallel_task_processing(2, 4, [2, 3, 4, 5]),
                         [(0, 0), (1, 0), (0, 2), (1, 3)])
        self.assertEqual(parallel_task_processing(2, 6, [1, 2, 3, 4, 5, 6]),
                         [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4), (1, 6)])


if __name__ == '__main__':
    unittest.main()
