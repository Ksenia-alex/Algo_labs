import tracemalloc
import time
from lab5.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def binary_search(mas, what_find):
    l = 0
    r = len(mas) - 1
    while l <= r:
        mid = (l + r) // 2
        if what_find == mas[mid]:
            return mid
        elif what_find < mas[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def play(mas, maas_find):
    return [binary_search(mas, maas_find[i]) for i in range(len(maas_find))]


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n, mass = int(lines[0]), list(map(int, lines[1].split()))
    k, mass_find = int(lines[2]), list(map(int, lines[3].split()))
    if 1 <= n <= 10 ** 5:
        result = play(mass, mass_find)
        write_file(' '.join(map(str, result)), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()