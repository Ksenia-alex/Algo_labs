from lab3.utils import read_coor, generations_str, write_str
from lab3.task8.src.task8 import count
import time
import tracemalloc

generations_str(8)

start = time.perf_counter()
tracemalloc.start()

n_k, data = read_coor()
n, k = n_k.split()

string = ''
for i in count(data, int(k)):
    string += str(i) + ','

write_str(string[:-1])

print(time.perf_counter() - start, 'c')
print(tracemalloc.get_traced_memory()[1] / 1024 / 1024, 'MB')
