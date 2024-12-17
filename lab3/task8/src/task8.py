import tracemalloc
import time
from lab3.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def dist(coor1: (float, float)) -> float:
    """Функция для нахождения расстояние между точкой и началом координат"""
    return coor1[0] ** 2 + coor1[1] ** 2


def count(coor: (float, float), k: int) -> [float]:
    """Функция для подсчета количества точек"""
    return [i[1] for i in sorted([(dist(cor), [cor[0], cor[1]]) for cor in coor])[:k]]


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n, k = lines[0].strip().split()
    data = [((float(i.strip().split()[0]), float(i.strip().split()[0]))) for i in lines[1:]]
    if 1 <= int(n) <= 5000:
        result = count(data, int(k))
        write_file(str(result), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()