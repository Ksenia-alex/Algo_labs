import time
import tracemalloc
import random

start = time.perf_counter()
tracemalloc.start()

# with open('input.txt', 'w') as f:
#     a = random.sample(range(100000), 1000)
#     f.write(' '.join(map(str, a)) + '\n')
#     f.write(' '.join(map(str, random.sample(a, 1))))


file = open('input.txt')
a = list(map(int, file.readline().split()))
v = int(file.readline())
ind = []
for i in range(len(a)):
    if a[i] == v:
        ind.append(i)


with open('output.txt', 'w') as file:
    if len(ind) == 0:
        file.write(str(-1))
    else:
        file.write(str(len(ind)) + ' ' + ', '.join(map(str, ind))) if len(ind) > 1 else file.write(str(ind[0]))

print(time.perf_counter() - start)
print(tracemalloc.get_traced_memory()[0] / 1024, 'MB')
