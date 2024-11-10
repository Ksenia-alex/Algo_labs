import unittest
import time
import tracemalloc
from lab2.Task3.task3 import search_inversions


class SearchInversionsTestCase(unittest.TestCase):
    def output_design(self, test_num, func, eq_value, *params):
        start = time.perf_counter()
        tracemalloc.start()
        self.assertEqual(func(params[0], params[1], params[2], params[3]), eq_value)

        print(f"Тест {test_num}:")
        print("Время работы: %s секунд " % (time.perf_counter() - start))
        print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
        tracemalloc.stop()

    def test_correctness(self):
        self.assertEqual(search_inversions([1, 8, 2, 1, 4, 7, 3, 2, 3, 6], [1, 8, 2, 1, 4, 7, 3, 2, 3, 6], 0, 9), 17)
        self.assertEqual(search_inversions([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 0, 4), 0)
        self.assertEqual(search_inversions([7, 5, 4, 3], [7, 5, 4, 3], 0, 3), 6)
        self.assertEqual(search_inversions([7, 5, 4, 3, 2, 1], [7, 5, 4, 3, 2, 1], 0, 5), 15)
        self.assertEqual(search_inversions([7, 5, 3, 23, 5, 4, 3], [7, 5, 3, 23, 5, 4, 3], 0, 6), 14)

    def test_time_memory(self):
        self.output_design(1, search_inversions, 17, [1, 8, 2, 1, 4, 7, 3, 2, 3, 6], [1, 8, 2, 1, 4, 7, 3, 2, 3, 6], 0, 9)
        self.output_design(2, search_inversions, 0, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 0, 4)
        self.output_design(3, search_inversions, 6, [7, 5, 4, 3], [7, 5, 4, 3], 0, 3)
