import tracemalloc
import time
from lab6.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def min_coins(money: int, coins: list[int]) -> float:
    """
    подсчет минимального количества момент с испоользованием дп
    :param money: int
    :param coins: list[int]
    :return: float
    """
    list_with_count_for_coints = [float('inf')] * (money + 1)
    list_with_count_for_coints[0] = 0
    for coin in coins:
        for i in range(coin, money + 1):
            list_with_count_for_coints[i] = min(list_with_count_for_coints[i], list_with_count_for_coints[i - coin] + 1)

    return list_with_count_for_coints[money]


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    money, k = map(int, lines[0].strip().split())
    coins = list(map(int, lines[1].split()))
    if 1 <= money <= 10 ** 3 and 1 <= k <= 100:
        result = min_coins(money, coins)
        write_file(str(result), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()