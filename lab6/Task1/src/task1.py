import tracemalloc
import time
from lab6.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def Set(operations):
    data = set()
    res = []
    for operation in operations:
        if operation.startswith("A"):
            data.add(operation.split()[1])
        elif operation.startswith("D"):
            data.remove(operation.split()[1])
        else:
            if operation.split()[1] in data:
                res.append("Y")
            else:
                res.append("N")
    return res


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    commands = [command.strip() for command in lines[1:]]
    if 1 <= len(commands) <= 5 * 10 ** 5:
        result = Set(commands)
        write_file('\n'.join(result), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()