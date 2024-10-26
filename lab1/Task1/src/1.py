import time
import random
import tracemalloc

tracemalloc.start()
start = time.perf_counter()

# with open('input.txt', 'w') as f:
#     f.write(str(1000) + '\n')
#     f.write(' '.join(map(str, list(reversed(sorted(random.sample(range(100000000), 1000)))))))

file = open('input.txt')
n = file.readline()
data = [int(i) for i in file.readline().split()]
file.close()


def insertion_sort(arr):
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i - 1
        while j >= 0 and item_to_insert < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = item_to_insert
    return arr


with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, insertion_sort(data))))

print(time.perf_counter() - start)
print(tracemalloc.get_traced_memory()[0] / 1024, 'MB')
