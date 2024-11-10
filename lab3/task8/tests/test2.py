import unittest
import time
import tracemalloc
from lab3.task8.src.task8 import count


class MinDistTestCase(unittest.TestCase):
    def output_design(self, test_num, func, eq_value, *params):
        start = time.perf_counter()
        tracemalloc.start()
        self.assertEqual(func(params[0], params[1]), eq_value)

        print(f"Тест {test_num}:")
        print("Время работы: %s секунд " % (time.perf_counter() - start))
        print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
        tracemalloc.stop()

    def test_correctness(self):
        self.assertEqual(count([(1, 3), (-2, 2)], 1), [[-2, 2]])
        self.assertEqual(count([(3, 3), (5, -1), (-2, 4)], 2), [[3, 3], [-2, 4]])

    def test_time_memory(self):
        self.output_design(1, count, [[-2, 2]], [(1, 3), (-2, 2)], 1)
        self.output_design(2, count, [[3, 3], [-2, 4]], [(3, 3), (5, -1), (-2, 4)], 2)
