import random


def generation():
    """Функция генерации рандомного массива из допустимого диапазона"""
    with open('input.txt', 'w') as file:
        n = random.randint(1, 10 ** 4 + 1)
        file.write(str(n) + '\n')
        file.write(' '.join(map(str, random.sample(range(10 ** 9), n))))


def read():
    """Функция чтения данных из файла"""
    file_input = open('input.txt')
    n, data = file_input.readline(), list(map(int, file_input.readline().split()))
    return n, data


def write(res):
    """Функция записи данных в файл"""
    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, res)))
