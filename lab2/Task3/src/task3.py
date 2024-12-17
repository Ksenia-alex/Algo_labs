import tracemalloc
import time
from lab5.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def search(mass, copy_mass, l, mid, r):
    i = k = l
    j = mid + 1
    count_inf = 0

    while i <= mid and j <= r:
        if mass[i] <= mass[j]:
            copy_mass[k] = mass[i]
            i += 1
        else:
            copy_mass[k] = mass[j]
            j += 1
            count_inf += (mid - i + 1)
        k += 1

    while i <= mid:
        copy_mass[k] = mass[i]
        k += 1
        i += 1

    for i in range(l, r + 1):
        mass[i] = copy_mass[i]
    return count_inf


def search_inversions(mass, copy_mass, l, r):
    if r <= l:
        return 0

    mid = (l + r) // 2
    count_inf = 0
    count_inf += search_inversions(mass, copy_mass, l, mid)
    count_inf += search_inversions(mass, copy_mass, mid + 1, r)
    count_inf += search(mass, copy_mass, l, mid, r)

    return count_inf


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    nums_copy = nums.copy()
    if 1 <= n <= 10 ** 5:
        result = search_inversions(nums, nums_copy, 0, n - 1)
        write_file(str(result), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()