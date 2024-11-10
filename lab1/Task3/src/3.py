import time
import random
import tracemalloc

tracemalloc.start()
start = time.perf_counter()

# with open('input.txt', 'w') as f:
#     f.write(str(1000) + '\n')
#     f.write(' '.join(map(str, random.sample(range(100000000), 1000))))

file = open('input.txt')
n = file.readline()
a = list(map(int, file.readline().split()))


def insertion_sort(a):
    for i in range(1, len(a)):
        item_to_insert = a[i]
        j = i - 1
        while j >= 0 and item_to_insert > a[j]:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = item_to_insert
    return a


with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, insertion_sort(a))))

print(time.perf_counter() - start)
print(tracemalloc.get_traced_memory()[0] / 1024, 'MB')
