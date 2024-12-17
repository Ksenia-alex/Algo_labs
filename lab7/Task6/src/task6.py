import tracemalloc
import time
from lab6.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def max_increasing_subsequence(numbers):
    n = len(numbers)
    if n == 0:
        return 0

    counts = [1] * n
    pred = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if numbers[j] < numbers[i]:
                counts[i] = max(counts[i], counts[j] + 1)
                pred[i] = j

    max_len = max(counts)
    index = counts.index(max_len)
    lis = []
    while index != -1:
        lis.append(numbers[index])
        index = pred[index]
    lis.reverse()

    return max(counts), lis


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = int(lines[0].strip())
    numders = list(map(int, lines[1].split()))
    if 1 <= n <= 300000:
        result = max_increasing_subsequence(numders)
        write_file('\n'.join([str(result[0]), ' '.join(map(str, result[1]))]), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()