import time

t_start = time.perf_counter()

n = int(open('input.txt').readline())
f = True
while f:
    if 0 <= n <= 10 ** 7:
        f = False
        break
    print('Неправильное значение n. Введите еще раз:')
    n = int(input())

first, second = 0, 1
for i in range(int(n) - 1):
    new = first + second
    first = second
    second = new
if n <= 1:
    new = n


with open('output.txt', 'w') as f:
    f.write(str(new % 10))
f.close()

print(time.perf_counter() - t_start)


