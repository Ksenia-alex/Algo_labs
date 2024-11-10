import random


def generation():
    """Функция генерации рандомного массива из допустимого диапазона"""
    with open('input.txt', 'w') as file:
        n = random.randint(1, 10 ** 4 + 1)
        file.write(str(n) + '\n')
        file.write(' '.join(map(str, random.sample(range(10 ** 9), n))))


def generations_str(number):
    with open('input.txt', 'w') as file:
        n = random.randint(1, 10 ** 5 + 1)
        if number == 8:
            k = random.randint(1, n)
            file.write(str(n) + ' ' + str(k) + '\n')
            for i in range(n):
                file.write(str(random.randint(-10 ** 9, 10 ** 9)) + ' ' + str(random.randint(-10 ** 9, 10 ** 9)) + '\n')
        if number == 9:
            file.write(str(n) + '\n')
            for i in range(n):
                file.write(str(random.randint(-10 ** 9, 10 ** 9)) + ' ' + str(random.randint(-10 ** 9, 10 ** 9)) + '\n')
        if number == 5:
            n = random.randint(1, 5000)
            string = ''
            for i in range(n):
                string += str(random.randint(0, 1000)) + ','
            file.write(string[:-1])



def read(number):
    """Функция чтения данных из файла"""
    file_input = open('input.txt')
    if number == 1 or number == 2:
        n, data = file_input.readline(), list(map(int, file_input.readline().split()))
        return n, data
    if number == 5:
        data = list(map(int, file_input.readline().split(',')))
        return data


def read_coor():
    file = open('input.txt')
    n = file.readline()
    coor = [(int(i.split()[0]), int(i.split()[1])) for i in file.readlines()]
    return n, coor


def write(res):
    """Функция записи данных в файл"""
    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, res)))


def write_str(res):
    """Функция записи строки в файл"""
    with open('output.txt', 'w') as file:
        file.write(str(res))