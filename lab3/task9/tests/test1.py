import time
import tracemalloc
from lab3.task9.src.task9 import min_distan
from lab3.utils import write_str, generations_str

start = time.perf_counter()
tracemalloc.start()

generations_str()

file = open('input.txt')
n = int(file.readline())
coor = [(int(i.split()[0]), int(i.split()[1])) for i in file.readlines()]

res = min_distan(coor)
write_str(res)

print(time.perf_counter() - start, 'c')
print(tracemalloc.get_traced_memory()[1] / 1024 / 1024, 'MB')
