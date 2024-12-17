import tracemalloc
import time
from lab6.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def solve(*args):
    n, x, a, b, ac, bc, ad, bd = args
    table = set()
    for _ in range(n):
        if x in table:
            a = (a + ac) % 10 ** 3
            b = (b + bc) % 10 ** 15
        else:
            table.add(x)
            a = (a + ad) % 10 ** 3
            b = (b + bd) % 10 ** 15
        x = (x * a + b) % 10 ** 15
    return x, a, b


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n, x, a, b = map(int, lines[0].split())
    ac, bc, ad, bd = map(int, lines[1].split())
    if 0 <= ac <= 10 ** 3 and 0 <= ad <= 10 ** 3 and 0 <= bc <= 10 ** 15 and 0 <= bd <= 10 ** 15:
        result = solve(n, x, a, b, ac, bc, ad, bd)
        write_file(' '.join(map(str, result)), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()