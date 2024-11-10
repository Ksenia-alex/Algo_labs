from lab3.utils import read, write_str, generations_str
from lab3.task5.src.task5 import find_index_h
import time
import tracemalloc

generations_str(5)

start = time.perf_counter()
tracemalloc.start()

arr = read(5)
write_str(find_index_h(arr))

print(time.perf_counter() - start)
print(tracemalloc.get_traced_memory()[1] / 1024 / 1024, 'MB')
