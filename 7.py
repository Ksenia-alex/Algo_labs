import time
import tracemalloc
import random

start = time.perf_counter()
tracemalloc.start()

# with open('input.txt', 'w') as f:
#     f.write(str(9999) + '\n')
#     f.write(' '.join(map(str, random.sample(range(100000000), 9999))))


file = open('input.txt')
n = int(file.readline())
a = file.readline().split()
m = sorted([(float(a[i]), i + 1) for i in range(len(a))])
res = [m[0][1], m[len(m) // 2][1], m[-1][1]]

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, res)))

print(time.perf_counter() - start)
print(tracemalloc.get_traced_memory()[0] / 1024, 'MB')
