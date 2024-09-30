import time
import tracemalloc
import random

start = time.perf_counter()
tracemalloc.start()

# with open('input.txt', 'w') as f:
#     f.write(str(1000) + '\n')
#     f.write(' '.join(map(str, random.sample(range(100000000), 1000))))

file = open('input.txt')
n = file.readline()
a = list(map(int, file.readline().split()))


def insertion_sort(arr):
    indx = [1]
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i - 1
        while j >= 0 and item_to_insert < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = item_to_insert
        indx.append(arr.index(item_to_insert) + 1)
    return indx, arr


with open('output.txt', 'w') as f:
    fun = insertion_sort(a)
    f.write(' '.join(map(str, fun[0])) + '\n')
    f.write(' '.join(map(str, fun[1])))

print(time.perf_counter() - start)
print(tracemalloc.get_traced_memory()[0] / 1024, 'MB')
