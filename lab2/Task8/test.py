import unittest
import time
import tracemalloc
from lab2.Task8.task8 import mul_polynomials


class PolynomialsMulTestCase(unittest.TestCase):
    def output_design(self, test_num, func, eq_value, *params):
        start = time.perf_counter()
        tracemalloc.start()
        self.assertEqual(func(params[0], params[1], params[2]), eq_value)

        print(f"Тест {test_num}:")
        print("Время работы: %s секунд " % (time.perf_counter() - start))
        print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
        tracemalloc.stop()

    def test_correctness(self):
        self.assertEqual(mul_polynomials([3, 2, 5], [5, 1, 2], 3), [15, 13, 33, 9, 10])
        self.assertEqual(mul_polynomials([2, 3, 4, 5, 6], [5, 6, 3, 1, 3], 5), [10, 27, 44, 60, 81, 64, 35, 21, 18])
        self.assertEqual(mul_polynomials([12, 23, 34, 45, 56], [1, 43, 45, 32, 23], 5), [12, 539, 1563, 2926, 4533, 6050, 4742, 2827, 1288])

    def test_time_memory(self):
        self.output_design(1, mul_polynomials, [15, 13, 33, 9, 10], [3, 2, 5], [5, 1, 2], 3)
        self.output_design(2, mul_polynomials, [10, 27, 44, 60, 81, 64, 35, 21, 18], [2, 3, 4, 5, 6], [5, 6, 3, 1, 3], 5)
        self.output_design(3, mul_polynomials, [12, 539, 1563, 2926, 4533, 6050, 4742, 2827, 1288], [12, 23, 34, 45, 56], [1, 43, 45, 32, 23], 5)
