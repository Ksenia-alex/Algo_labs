import tracemalloc
import time
from lab5.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def find_max(a):
    max_sum, summ = 0, 0
    for i in range(len(a)):
        if summ == 0:
            start_indx = i
        summ += a[i]
        if max_sum < summ:
            max_sum = summ
            end_indx = i
        if summ < 0:
            summ = 0
    return a[start_indx:end_indx + 1]


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    nums = list(map(int, lines[0].split()))
    if 1 <= len(nums) <= 10 ** 5:
        result = find_max(nums)
        write_file(str(result), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()