import time
import tracemalloc
from lab2.Task3.task3 import search_inversions
import random


def max_input():
    with open('input.txt', 'w') as file:
        file.write(str(10 ** 5) + '\n')
        file.write(' '.join(map(str, random.sample(range(10 ** 9), 10 ** 5))))

    start = time.perf_counter()
    tracemalloc.start()

    with open('output.txt', 'w') as f:
        file = open('input.txt')
        n = int(file.readline())
        mass = list(map(int, file.readline().split()))
        mass_copy = mass.copy()
        f.write(str(search_inversions(mass, mass_copy, 0, n - 1)))

    print('Для максимальных значений:')
    print("Время работы: %s секунд " % (time.perf_counter() - start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


def min_input():
    with open('input.txt', 'w') as file:
        file.write(str(1) + '\n')
        file.write(str(1))

    start = time.perf_counter()
    tracemalloc.start()

    with open('output.txt', 'w') as f:
        file = open('input.txt')
        n = int(file.readline())
        mass = list(map(int, file.readline().split()))
        mass_copy = mass.copy()
        f.write(str(search_inversions(mass, mass_copy, 0, n - 1)))

    print('Для минимальных значений:')
    print("Время работы: %s секунд " % (time.perf_counter() - start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
    tracemalloc.stop()


min_input()
print()
max_input()
