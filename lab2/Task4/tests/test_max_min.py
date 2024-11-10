import time
import tracemalloc
from lab2.Task4.task4 import play
import random


def max_input():
    with open('input.txt', 'w') as file:
        file.write(str(10 ** 5) + '\n')
        list_input = random.sample(range(10 ** 9), 10 ** 5)
        file.write(' '.join(map(str, sorted(list_input))) + '\n')
        file.write(str(10 ** 5) + '\n')
        file.write(' '.join(map(str, random.sample(random.sample(range(10 ** 9), 99000) + random.sample(list_input, 10 ** 3), 10 ** 5))))

    start = time.perf_counter()
    tracemalloc.start()

    with open('output.txt', 'w') as f:
        file = open('input.txt')
        n, mass = int(file.readline()), list(map(int, file.readline().split()))
        k, mass_find = int(file.readline()), list(map(int, file.readline().split()))
        f.write(' '.join(map(str, play(mass, mass_find))))

    print('Для максимальных значений:')
    print("Время работы: %s секунд " % (time.perf_counter() - start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


def min_input():
    with open('input.txt', 'w') as file:
        file.write(str(1) + '\n')
        file.write(str(1) + '\n')
        file.write(str(1) + '\n')
        file.write(str(1) + '\n')

    start = time.perf_counter()
    tracemalloc.start()

    with open('output.txt', 'w') as f:
        file = open('input.txt')
        n, mass = int(file.readline()), list(map(int, file.readline().split()))
        k, mass_find = int(file.readline()), list(map(int, file.readline().split()))
        f.write(' '.join(map(str, play(mass, mass_find))))

    print('Для минимальных значений:')
    print("Время работы: %s секунд " % (time.perf_counter() - start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


max_input()
print()
min_input()
