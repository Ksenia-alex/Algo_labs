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

def bubble_sorting(a, direction):
    if direction == 'По возрастанию':
        k = 1
    else:
        k = -1
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if k * a[j] > k * a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, bubble_sorting(a, 'По убыванию'))))

print(time.perf_counter() - start)
print(tracemalloc.get_traced_memory()[0] / 1024, 'MB')
