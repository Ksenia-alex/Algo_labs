import time
import tracemalloc
import random

start = time.perf_counter()
tracemalloc.start()

# with open('input.txt', 'w') as f:
#     f.write(str(5000) + '\n')
#     f.write(' '.join(map(str, random.sample(range(100000000), 5000))))


file = open('input.txt')
n = int(file.readline())
a = [int(i) for i in file.readline().split()]

with open('output.txt', 'w') as file:
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                file.write(f'Swap elements at indices {j} and {j + 1}.\n')
    file.write('No mare swaps needed')

print(time.perf_counter() - start)
print(tracemalloc.get_traced_memory()[0] / 1024, 'MB')