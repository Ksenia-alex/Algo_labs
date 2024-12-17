import tracemalloc
import time
from lab5.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def mul_polynomials(a, b, n):
    res = [0] * (n + n - 1)
    for cof_a in range(n):
        for cof_b in range(n):
            res[cof_a + cof_b] += a[cof_b] * b[cof_a]
    return res


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = int(lines[0])
    a, b = list(map(int, lines[1].split())), list(map(int, lines[2].split()))
    result = mul_polynomials(a, b, n)
    write_file(str(result), OUTPUT_PATH)

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()