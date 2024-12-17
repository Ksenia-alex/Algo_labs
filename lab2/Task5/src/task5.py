import tracemalloc
import time
from lab5.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def majority(a):
    dic = {}
    for i in a:
        dic[i] = dic.get(i, 0) + 1

    for k, v in dic.items():
        if v > len(a) // 2:
            return 1
    return 0


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = int(lines[0])
    list_input = list(map(int, lines[1].split()))
    if 1 <= n <= 10 ** 5:
        result = majority(list_input)
        write_file(str(result), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()