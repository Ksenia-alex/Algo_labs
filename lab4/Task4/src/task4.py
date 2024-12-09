import tracemalloc
import time
from lab4.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def checking_bracket_sequence(string: str) -> str:
    bracket = {")": "(", "}": "{", "]": "["}
    stack = []
    for i, char in enumerate(string, 1):
        if char in "([{":
            stack.append((i, char))
        elif char in "}])":
            if not stack:
                return str(i)
            pos, top_char_stack = stack.pop()
            if top_char_stack != bracket[char]:
                return str(pos)
    if stack:
        pos, top_char_stack = stack.pop()
        return str(pos)
    return "Success"


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")


if __name__ == "__main__":
    string_with_bracket = open_file(INPUT_PATH)[0].strip()

    if 1 <= len(string_with_bracket) <= 10 ** 5:
        results = checking_bracket_sequence(string_with_bracket)
        write_file(results, OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
