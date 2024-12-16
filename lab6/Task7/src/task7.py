import tracemalloc
import time
from lab6.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def count_beautiful_pairs(n, S, beautiful_pairs):
    beautiful_set = set(beautiful_pairs)
    freq = [0] * 26
    total_pairs = 0

    for i in range(n):
        current_char = S[i]
        for a, b in beautiful_set:
            if current_char == b:
                total_pairs += freq[ord(a) - ord('a')]
        freq[ord(current_char) - ord('a')] += 1
    return total_pairs


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n, k = lines[0].split()
    S = lines[1].strip()
    beautiful_pairs = [(i[0], i[1]) for i in lines[2:]]
    if 1 <= int(n) <= 10 ** 5 and 1 <= int(k) <= 676:
        result = count_beautiful_pairs(int(n), S, beautiful_pairs)
        write_file(str(result), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()