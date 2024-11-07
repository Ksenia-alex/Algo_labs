import random
from lab3.utils import read, write
from lab3.task2.src.task2 import generation_test_for_max_swap
import time
import tracemalloc


def generation():
    """Функция генерации рандомного массива из допустимого диапазона"""
    with open('input.txt', 'w') as file:
        n = random.randint(1, 10 ** 6)
        file.write(str(n))


generation()
start = time.perf_counter()
tracemalloc.start()

n, data = read()
res = generation_test_for_max_swap(int(n))
write(res)

print(time.perf_counter() - start, 'c')
print(tracemalloc.get_traced_memory()[1] / 1024 / 1024, 'MB')
tracemalloc.stop()



