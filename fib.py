n = int(open('/Users/kseniatolstuhina/PycharmProjects/pythonProject/Task 2/input.txt').readline())
f = True
while f:
    if 0 <= n <= 45:
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
with open('/Users/kseniatolstuhina/PycharmProjects/pythonProject/Task 2/output.txt', 'w') as f:
    f.write(str(new))
f.close()
