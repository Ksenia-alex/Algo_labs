import time
import tracemalloc

start = time.perf_counter()
tracemalloc.start()

file = open('input.txt')
n = int(file.readline())
list_let = list(file.readline())
dict = {}
res = ''

for ch in list_let:
    if ch not in dict.keys():
        dict[ch] = 1
    else:
        dict[ch] += 1
        if dict[ch] == 2:
            res += ch
            dict[ch] = 0

res = ''.join(sorted(res))
list_mid = []
for ch, count in dict.items():
    if count == 1:
        list_mid.append(ch)

with open('output.txt', 'w') as file:
    if list_mid:
        file.write(res + str(sorted(list_mid)[0]) + res[::-1])
    else:
        file.write(res + res[::-1])

print(time.perf_counter() - start)
print(tracemalloc.get_traced_memory()[0] / 1024, 'MB')
