def find_max(a):
    max_sum, summ = 0, 0
    for i in range(len(a)):
        if summ == 0:
            start_indx = i
        summ += a[i]
        if max_sum < summ:
            max_sum = summ
            end_indx = i
        if summ < 0:
            summ = 0
    return a[start_indx:end_indx + 1]


with open('output.txt', 'w') as file:
    f_input = list(map(int, open('input.txt').readline().split()))
    a = find_max(f_input)
    file.write(' '.join(map(str, a)))
