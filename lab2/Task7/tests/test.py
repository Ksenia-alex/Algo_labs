import unittest
import time
import tracemalloc
from lab2.Task7.src.task7 import find_max

class InsertionSortTestCase(unittest.TestCase):
    def output_design(self, test_num, func, eq_value, params):
        start = time.perf_counter()
        tracemalloc.start()
        self.assertEqual(func(params), eq_value)

        print(f"Тест {test_num}:")
        print("Время работы: %s секунд " % (time.perf_counter() - start))
        print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
        tracemalloc.stop()

    def test_correctness(self):
        self.assertEqual(find_max([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]), [18, 20, -7, 12])
        self.assertEqual(find_max([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(find_max([2, -2, -5, -60, 1, 9, 1, 2]),[1, 9, 1, 2])

    def test_time_memory(self):
        self.output_design(1, find_max, [18, 20, -7, 12], [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
        self.output_design(2, find_max, [1, 2, 3, 4],[1, 2, 3, 4])
        self.output_design(3, find_max, [1, 9, 1, 2],[2, -2, -5, -60, 1, 9, 1, 2])
        self.output_design(4, find_max, [1], [1])

