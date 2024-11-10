import unittest
import time
import tracemalloc
from lab3.task5.src.task5 import find_index_h


class MinDistTestCase(unittest.TestCase):
    def output_design(self, test_num, func, eq_value, params):
        start = time.perf_counter()
        tracemalloc.start()
        self.assertEqual(func(params), eq_value)

        print(f"Тест {test_num}:")
        print("Время работы: %s секунд " % (time.perf_counter() - start))
        print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
        tracemalloc.stop()

    def test_correctness(self):
        self.assertEqual(find_index_h([3, 0, 6, 1, 5]), 3)
        self.assertEqual(find_index_h([1, 3, 1]), 1)
        self.assertEqual(find_index_h([1, 5, 7, 2, 8, 0, 2, 5, 2, 4]), 4)


    def test_time_memory(self):
        self.output_design(1, find_index_h, 3, [3, 0, 6, 1, 5])
        self.output_design(2, find_index_h, 1, [1, 3, 1])
        self.output_design(3, find_index_h, 4, [1, 5, 7, 2, 8, 0, 2, 5, 2, 4])
