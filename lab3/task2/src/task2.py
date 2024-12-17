import tracemalloc
import time
from lab3.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def generation_test_for_max_swap(n):
    """функция генерации теста"""
    return list(reversed(sorted(range(1, n + 1))))


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = lines[0]
    if 1 <= int(n) <= 10 ** 6:
        result = generation_test_for_max_swap(int(n))
        write_file(' '.join(map(str, result)), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()