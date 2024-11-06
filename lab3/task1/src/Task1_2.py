import random


def partition(arr, left, right):
    """функция разбиения массива на три части
    >>> a = [4, 3, 9, 2, 2, 1, 4, 10]
    >>> partition(a, 0, len(a) - 1)
    (4, 5)
    >>> b = [5, 2, 3, 1]
    >>> partition(b, 0, len(b) - 1)
    (3, 3)
    """
    x = arr[left]
    m1 = left
    m2 = right
    i = left + 1
    while i <= m2:
        if arr[i] < x:
            m1 += 1
            arr[m1], arr[i] = arr[i], arr[m1]
            i += 1
        elif arr[i] > x:
            arr[i], arr[m2] = arr[m2], arr[i]
            m2 -= 1
        else:
            i += 1
    arr[left], arr[m1] = arr[m1], arr[left]
    return m1, m2


def randomizer_quicksort(arr, left, right):
    """Функция рандомизированной сортировки массива
    >>> a = [2, 3, 9, 2, 2]
    >>> randomizer_quicksort(a, 0, len(a) - 1)
    >>> a
    [2, 2, 2, 3, 9]
    >>> a = [4, 3, 9, 2, 2, 1, 4, 10]
    >>> randomizer_quicksort(a, 0, len(a) - 1)
    >>> a
    [1, 2, 2, 3, 4, 4, 9, 10]
    """
    if left < right:
        k = random.randint(left, right)
        arr[left], arr[k] = arr[k], arr[left]
        m1, m2 = partition(arr, left, right)
        randomizer_quicksort(arr, left, m1 - 1)
        randomizer_quicksort(arr, m2 + 1, right)

