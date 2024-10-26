file = open('input.txt')
n, mass = int(file.readline()), list(map(int, file.readline().split()))
k, mass_find = int(file.readline()), list(map(int, file.readline().split()))


def binary_search(mas, what_find):
    l = 0
    r = len(mas) - 1
    while l <= r:
        mid = (l + r) // 2
        if what_find == mas[mid]:
            return mid
        elif what_find < mas[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def play(mas, maas_find):
    return [binary_search(mas, maas_find[i]) for i in range(len(maas_find))]


with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, play(mass, mass_find))))
