import random
import tracemalloc
import time
from lab6.utils import *

t_start = time.perf_counter()
tracemalloc.start()

# with open('input.txt', 'w') as f:
#     f.write(str(1000) + '\n')
#     f.write(' '.join(map(str, list(reversed(sorted(random.sample(range(100000000), 1000)))))))


def insertion_sort(arr):
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i - 1
        while j >= 0 and item_to_insert < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = item_to_insert
    return arr


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = int(lines[0])
    data = [int(i) for i in lines[1].split()]
    if 1 <= n <= 5 * 10 ** 5:
        write_file(' '.join(map(str, insertion_sort(data))), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()