import time
import random
import tracemalloc

start = time.perf_counter()
tracemalloc.start()

# with open('input.txt', 'w') as f:
#     f.write(str(1000) + '\n')
#     f.write(' '.join(map(str, list(reversed(sorted(random.sample(range(100000000), 1000)))))))

file = open('input.txt')
n = int(file.readline())
arr = list(map(int, file.readline().split()))

for i in range(len(arr) - 1):
    min_el = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_el]:
            min_el = j
    arr[i], arr[min_el] = arr[min_el], arr[i]


with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, arr)))

print(time.perf_counter() - start)
print(tracemalloc.get_traced_memory()[0] / 1024, 'Mb')