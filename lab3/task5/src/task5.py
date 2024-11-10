def find_index_h(arr: [int]) -> int:
    """"Функция для нахождения индекса Хирша"""
    return sorted(arr)[::-1][round(len(arr) / 2)]
