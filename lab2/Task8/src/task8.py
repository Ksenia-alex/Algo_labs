def mul_polynomials(a, b, n):
    res = [0] * (n + n - 1)
    for cof_a in range(n):
        for cof_b in range(n):
            res[cof_a + cof_b] += a[cof_b] * b[cof_a]
    return res


with open('output.txt', 'w') as f:
    file = open('input.txt')
    n = int(file.readline())
    a, b = list(map(int, file.readline().split())), list(map(int, file.readline().split()))
    f.write(' '.join(map(str, mul_polynomials(a, b, n))))
