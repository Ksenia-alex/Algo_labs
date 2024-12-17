import random
import tracemalloc
import time
from lab3.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def partition(arr, left, right):
    """функция разбиения массива на три части
    >>> a = [4, 3, 9, 2, 2, 1, 4, 10]
    >>> partition(a, 0, len(a) - 1)
    (4, 5)
    >>> b = [5, 2, 3, 1]
    >>> partition(b, 0, len(b) - 1)
    (3, 3)
    """
    x = arr[left]
    m1 = left
    m2 = right
    i = left + 1
    while i <= m2:
        if arr[i] < x:
            m1 += 1
            arr[m1], arr[i] = arr[i], arr[m1]
            i += 1
        elif arr[i] > x:
            arr[i], arr[m2] = arr[m2], arr[i]
            m2 -= 1
        else:
            i += 1
    arr[left], arr[m1] = arr[m1], arr[left]
    return m1, m2


def randomizer_quicksort(arr, left, right):
    """Функция рандомизированной сортировки массива
    >>> a = [2, 3, 9, 2, 2]
    >>> randomizer_quicksort(a, 0, len(a) - 1)
    >>> a
    [2, 2, 2, 3, 9]
    >>> a = [4, 3, 9, 2, 2, 1, 4, 10]
    >>> randomizer_quicksort(a, 0, len(a) - 1)
    >>> a
    [1, 2, 2, 3, 4, 4, 9, 10]
    """
    if left < right:
        k = random.randint(left, right)
        arr[left], arr[k] = arr[k], arr[left]
        m1, m2 = partition(arr, left, right)
        randomizer_quicksort(arr, left, m1 - 1)
        randomizer_quicksort(arr, m2 + 1, right)


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = lines[0]
    data = list(map(int, lines[1].split()))
    if 1 <= int(n) <= 10 ** 4:
        randomizer_quicksort(data, 0, len(data) - 1)
        write_file(' '.join(map(str, data)), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
