import time
import tracemalloc
import random

tracemalloc.start()
start = time.perf_counter()

# with open('input.txt', 'w') as f:
#     f.write(str(1000) + '\n')
#     f.write(' '.join(map(str, list(reversed(sorted(random.sample(range(100000000), 1000)))))))


file = open('input.txt')
n = int(file.readline())
a = list(map(int, file.readline().split()))

for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, a)))

print(time.perf_counter() - start)
print(tracemalloc.get_traced_memory()[0] / 1024, 'MB')