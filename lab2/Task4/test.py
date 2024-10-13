import unittest
import time
import tracemalloc
from lab2.Task4.task4 import play


class BinarySearchTestCase(unittest.TestCase):
    def output_design(self, test_num, func, eq_value, *params):
        start = time.perf_counter()
        tracemalloc.start()
        self.assertEqual(func(params[0], params[1]), eq_value)

        print(f"Тест {test_num}:")
        print("Время работы: %s секунд " % (time.perf_counter() - start))
        print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
        tracemalloc.stop()

    def test_correctness(self):
        self.assertEqual(play([1, 5, 8, 12, 13], [8, 1, 23, 1, 11]), [2, 0, -1, 0, -1])
        self.assertEqual(play([3, 5, 7, 9], [1, 9, 10, 0, 7, 7]), [-1, 3, -1, -1, 2, 2])
        self.assertEqual(play([12, 23, 34, 45, 56, 67], [0, 43, 45, 32, 23]), [-1, -1, 3, -1, 1])

    def test_time_memory(self):
        self.output_design(1, play, [2, 0, -1, 0, -1], [1, 5, 8, 12, 13], [8, 1, 23, 1, 11])
        self.output_design(2, play, [-1, 3, -1, -1, 2, 2], [3, 5, 7, 9], [1, 9, 10, 0, 7, 7])
        self.output_design(3, play, [-1, -1, 3, -1, 1], [12, 23, 34, 45, 56, 67], [0, 43, 45, 32, 23])
