import tracemalloc
import time
from lab3.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def find_index_h(arr: [int]) -> int:
    """"Функция для нахождения индекса Хирша"""
    arr.sort(reverse=True)
    for i, count_citation in enumerate(arr, 1):
        if count_citation < i:
            return i - 1
    return len(arr)


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    data = [int(i) for i in lines[0].split(',')]
    if 1 <= len(data) <= 5000:
        result = find_index_h(data)
        write_file(str(result), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()