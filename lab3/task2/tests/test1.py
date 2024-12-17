import unittest
from lab3.task2.src.task2 import generation_test_for_max_swap


class TestCase(unittest.TestCase):
    def test_with_data_task(self):
        self.assertEqual(generation_test_for_max_swap(3), [3, 2, 1])

    def test_with_other_data(self):
        self.assertEqual(generation_test_for_max_swap(1), [1])
        self.assertEqual(generation_test_for_max_swap(6), [6, 5, 4, 3, 2, 1])
        self.assertEqual(generation_test_for_max_swap(4), [4, 3, 2, 1])
        self.assertEqual(generation_test_for_max_swap(7), [7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(generation_test_for_max_swap(2), [2, 1])



if __name__ == '__main__':
    unittest.main()