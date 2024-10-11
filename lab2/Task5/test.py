import random
import time
import tracemalloc
from lab2.Task5.task5 import majority

with open('input.txt', 'w') as file:
    file.write(str(10 ** 5) + '\n')
    file.write(' '.join(map(str, random.sample(range(10 ** 9), 10 ** 5))))

start = time.perf_counter()
tracemalloc.start()

with open('output.txt', 'w') as f:
    file = open('input.txt')
    n = int(file.readline())
    list_input = list(map(int, file.readline().split()))
    f.write(str(majority(list_input)))

print(time.perf_counter() - start, 'c')
print(tracemalloc.get_traced_memory()[1] / 1024 / 1024, 'MB')
