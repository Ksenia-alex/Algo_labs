def majority(a):
    dic = {}
    for i in a:
        dic[i] = dic.get(i, 0) + 1

    for k, v in dic.items():
        if v > len(a) // 2:
            return 1
    return 0


with open('output.txt', 'w') as f:
    file = open('input.txt')
    n = int(file.readline())
    list_input = list(map(int, file.readline().split()))
    f.write(str(majority(list_input)))
