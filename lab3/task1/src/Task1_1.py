import random


def partition(arr, left, right):
    """Функция для разбиения массива на два подмассива
    >>> a = [2, 4, 1, 2, 5]
    >>> partition(a, 0, len(a) - 1)
    4
    >>> b = [2, 2, 4, 1, 1, 7]
    >>> partition(b, 0, len(b) -1)
    5
    """
    x = arr[right]
    j = left
    for i in range(left, right):
        if arr[i] <= x:
            arr[j], arr[i] = arr[i], arr[j]
            j = j + 1
    arr[right], arr[j] = arr[j], arr[right]
    return j


def randomizer_quicksort(arr, left, right):
    """Функция для сортировки массива
    >>> a = [2, 4, 1, 2, 5]
    >>> randomizer_quicksort(a, 0, len(a) - 1)
    >>> a
    [1, 2, 2, 4, 5]
    >>> b = [4, 3, 9, 2, 2, 1, 4, 10]
    >>> randomizer_quicksort(b, 0, len(b) - 1)
    >>> b
    [1, 2, 2, 3, 4, 4, 9, 10]
    """
    if left >= right:
        return
    if left < right:
        k = random.randint(left, right)
        arr[right], arr[k] = arr[k], arr[right]
        m = partition(arr, left, right)
        randomizer_quicksort(arr, left, m - 1)
        randomizer_quicksort(arr, m + 1, right)


