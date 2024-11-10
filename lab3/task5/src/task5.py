def find_index_h(arr: [int]) -> int:
    """"Функция для нахождения индекса Хирша"""
    arr.sort(reverse=True)
    for i, count_citation in enumerate(arr, 1):
        if count_citation < i:
            return i - 1
    return len(arr)
