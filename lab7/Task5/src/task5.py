import tracemalloc
import time
from lab7.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def max_increasing_subsequence(number1: list[int], number2: list[int], number3: list[int]) -> int:
    """
    находит максимальную длину общей подпоследовательности трех последовательностей
    :param number1: list[int]
    :param number2: list[int]
    :param number3: list[int]
    :return: int
    """
    counts = [[[0] * (len(number3) + 1) for _ in range(len(number2) + 1)] for _ in range(len(number1) + 1)]

    for i in range(1, len(number1) + 1):
        for j in range(1, len(number2) + 1):
            for k in range(1, len(number3) + 1):
                if number1[i - 1] == number2[j - 1] == number3[k - 1]:
                    counts[i][j][k] = counts[i - 1][j - 1][k - 1] + 1
                else:
                    counts[i][j][k] = max(counts[i][j][k - 1], counts[i][j - 1][k], counts[i - 1][j][k])
    return counts[len(number1)][len(number2)][len(number3)]


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = int(lines[0].strip())
    numders1 = list(map(int, lines[1].split()))
    m = int(lines[2].strip())
    numders2 = list(map(int, lines[3].split()))
    k = int(lines[4].strip())
    numders3 = list(map(int, lines[5].split()))
    if 1 <= n <= 100 and 1 <= m <= 100 and 1 <= k <= 100:
        result = max_increasing_subsequence(numders1, numders2, numders3)
        write_file(str(result), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()