import unittest
import time
import tracemalloc
from lab2.Task5.src.task5 import majority


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
        self.assertEqual(majority([8, 1, 23, 1, 11]), 0)
        self.assertEqual(majority([1, 1, 1, 3, 4, 5]), 0)
        self.assertEqual(majority([2, 3, 9, 2, 2]), 1)
        self.assertEqual(majority([1, 2, 3, 4]), 0)
        self.assertEqual(majority([2, 1, 9, 1, 2]), 0)

    def test_time_memory(self):
        self.output_design(1, majority, 1, [2, 3, 9, 2, 2])
        self.output_design(2, majority, 0,[1, 2, 3, 4])
        self.output_design(3, majority, 0,[2, 1, 9, 1, 2])
