from lab3.utils import generation, read, write
from lab3.task1.src.Task1_2 import randomizer_quicksort
import tracemalloc
import time

generation()
start = time.perf_counter()
tracemalloc.start()
n, data = read()

randomizer_quicksort(data, 0, len(data) - 1)
write(data)
print(time.perf_counter() - start, 'c')
print(tracemalloc.get_traced_memory()[1] / 1024 / 1024, 'MB')