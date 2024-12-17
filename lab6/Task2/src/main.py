import tracemalloc
import time
from lab6.utils import *
from lab6.Task2.src.ClassPhoneBook import PhoneBook

t_start = time.perf_counter()
tracemalloc.start()


def main(commands):
    res = []
    phone_book = PhoneBook()
    for command in commands:
        if command.startswith("add"):
            _, number, name = command.split()
            phone_book.add_person(name, int(number))
        elif command.startswith("del"):
            _, number = command.split()
            phone_book.del_number(int(number))
        else:
            _, number = command.split()
            res.append(phone_book.find_number(int(number)))
    return res


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    commands = [command.strip() for command in lines[1:]]
    if 1 <= len(commands) <= 10 ** 5:
        result = main(commands)
        write_file('\n'.join(result), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
