def search(mass, copy_mass, l, mid, r):
    i = k = l
    j = mid + 1
    count_inf = 0

    while i <= mid and j <= r:
        if mass[i] <= mass[j]:
            copy_mass[k] = mass[i]
            i += 1
        else:
            copy_mass[k] = mass[j]
            j += 1
            count_inf += (mid - i + 1)
        k += 1

    while i <= mid:
        copy_mass[k] = mass[i]
        k += 1
        i += 1

    for i in range(l, r + 1):
        mass[i] = copy_mass[i]
    return count_inf


def search_inversions(mass, copy_mass, l, r):
    if r <= l:
        return 0

    mid = (l + r) // 2
    count_inf = 0
    count_inf += search_inversions(mass, copy_mass, l, mid)
    count_inf += search_inversions(mass, copy_mass, mid + 1, r)
    count_inf += search(mass, copy_mass, l, mid, r)

    return count_inf


with open('output.txt', 'w') as f:
    file = open('input.txt')
    n = int(file.readline())
    nums = list(map(int, file.readline().split()))
    nums_copy = nums.copy()
    f.write(str(search_inversions(nums, nums_copy, 0, n - 1)))
