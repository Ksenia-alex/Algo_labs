import tracemalloc
import time
import random
from lab6.utils import *

t_start = time.perf_counter()
tracemalloc.start()


# with open('input.txt', 'w') as f:
#     a = random.sample(range(100000), 1000)
#     f.write(' '.join(map(str, a)) + '\n')
#     f.write(' '.join(map(str, random.sample(a, 1))))


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    a = list(map(int, lines[0].split()))
    v = int(lines[1])
    ind = []
    for i in range(len(a)):
        if a[i] == v:
            ind.append(i)
    if 1 <= v <= 5 * 10 ** 5:
        write_file(str(len(ind)) + ' ' + ', '.join(map(str, ind)), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()