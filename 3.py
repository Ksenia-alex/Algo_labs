with open('input.txt', 'r') as f:
    a, b = map(int, f.readline().split())
    flag = True
    while f:
        if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= b <= 10 ** 9:
            flag = False
            break
        print('Неккоректные данные. Введите еще раз:')
        a, b = map(int, input().split())

f.close()

with open('output.txt', 'w') as f:
    f.write(str(a + b))

f.close()