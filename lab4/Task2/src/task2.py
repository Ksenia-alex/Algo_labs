import tracemalloc
import time
from lab4.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def algo_queue(commands: list[str]) -> list[str]:
    """
    Обрабатывает команды работы с очередью.
    commands: Список строк, содержащих команды (+ N или -)
    """
    queue = []
    res = []
    for command in commands:
        if command.startswith("+"):
            cmd, number = command.split()
            queue.append(number)
        elif command == "-":
            res.append(queue.pop(0))

    return res


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")


if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    commands = [command.strip() for command in lines[1:]]

    if 1 <= len(commands) <= 10 ** 6:
        results = algo_queue(commands)
        write_file("\n".join(results), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
