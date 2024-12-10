import tracemalloc
import time
from lab4.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def postfix_entry(chars: list[str]) -> int:
    """
    вычисляет значение выражения
    :param chars: list[str]
    :return: list[str]
    """
    stack = []
    for char in chars:
        if char in '0123456789':
            stack.append(int(char))
        if char == '+':
            second = stack.pop()
            first = stack.pop()
            stack.append(first + second)
        if char == '-':
            second = stack.pop()
            first = stack.pop()
            stack.append(first - second)
        if char == '*':
            second = stack.pop()
            first = stack.pop()
            stack.append(first * second)
    return stack[0]


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")


if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    chars = lines[1].split()

    if 1 <= len(chars) <= 10 ** 6:
        results = postfix_entry(chars)
        write_file(str(results), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
