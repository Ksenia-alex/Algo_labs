import time
import tracemalloc
import random

start = time.perf_counter()
tracemalloc.start()

file = open('input.txt')
a, b = file.readline().split()

with open('output.txt', 'w') as file:
    file.write(bin(int(a, 2) + int(b, 2))[2:])

print(time.perf_counter() - start)
print(tracemalloc.get_traced_memory()[0] / 1024)
