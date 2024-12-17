import time
import tracemalloc
import random
from lab2.Task7.task7 import find_max

start = time.perf_counter()
tracemalloc.start()

with open('../txtf/input.txt', 'w') as f:
    f.write(' '.join(map(str, random.sample(range(-10 ** 9, 10 ** 9), 2 * 10 ** 4))))

with open('../txtf/output.txt', 'w') as file:
    f_input = list(map(int, open('../txtf/input.txt').readline().split()))
    a = find_max(f_input)
    file.write(' '.join(map(str, a)))


print("Время работы: %s секунд " % (time.perf_counter() - start))
print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
