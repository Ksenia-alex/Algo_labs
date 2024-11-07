import unittest
import time
import tracemalloc
from lab3.task9.src.task9 import min_distan


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
        self.assertEqual(min_distan([(0, 0), (3, 4)]), 5.0)
        self.assertEqual(min_distan([(7, 7), (1, 100), (2, 4), (7, 7)]), 0.0)
        self.assertEqual(min_distan([(4, 4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0), (1, 1), (-1, -1), (3, -1), (-4, 2), (-2, 4)]), 1.4142136)


    def test_time_memory(self):
        self.output_design(1, min_distan, 5.0, [(0, 0), (3, 4)])
        self.output_design(2, min_distan, 0.0, [(7, 7), (1, 100), (2, 4), (7, 7)])
        self.output_design(3, min_distan, 1.4142136, [(4, 4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0), (1, 1), (-1, -1), (3, -1), (-4, 2), (-2, 4)])
