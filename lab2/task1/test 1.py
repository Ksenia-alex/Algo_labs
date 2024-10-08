import random
import time
import tracemalloc
from lab2.task1.task1 import merge_sort

start = time.perf_counter()
tracemalloc.start()


def average_case():
    with open('input.txt', 'w') as file:
        n = random.randint(1, 2 * 10 ** 4)
        file.write(str(n) + '\n')
        file.write(' '.join(map(str, random.sample(range(1000000), n))))

    with open('output.txt', 'w') as f:
        file = open('input.txt')
        n = int(file.readline())
        nums = list(map(int, file.readline().split()))
        f.write(' '.join(map(str, merge_sort(nums))))


def worst_case():
    with open('input.txt', 'w') as file:
        n = random.randint(1, 2 * 10 ** 4)
        file.write(str(n) + '\n')
        file.write(' '.join(map(str, sorted(random.sample(range(1000000), n))[::-1])))

    with open('output.txt', 'w') as f:
        file = open('input.txt')
        n = int(file.readline())
        nums = list(map(int, file.readline().split()))
        f.write(' '.join(map(str, merge_sort(nums))))


def better_case():
    with open('input.txt', 'w') as file:
        n = random.randint(1, 2 * 10 ** 4)
        file.write(str(n) + '\n')
        file.write(' '.join(map(str, sorted(random.sample(range(1000000), n)))))

    with open('output.txt', 'w') as f:
        file = open('input.txt')
        n = int(file.readline())
        nums = list(map(int, file.readline().split()))
        f.write(' '.join(map(str, merge_sort(nums))))


# better_case()
# print(time.perf_counter() - start, 'c', sep='')
# print(tracemalloc.get_traced_memory()[0] / 1024, 'MB')
#
# worst_case()
# print(time.perf_counter() - start, 'c', sep='')
# print(tracemalloc.get_traced_memory()[0] / 1024, 'MB')
#
# average_case()
# print(time.perf_counter() - start, 'c', sep='')
# print(tracemalloc.get_traced_memory()[0] / 1024, 'MB')
