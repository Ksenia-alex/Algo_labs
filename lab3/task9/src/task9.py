import math


def dist(coor1, coor2):
    """Функция для нахождения расстояния между координатами"""
    return math.dist(coor1, coor2)


def recurse(coor_x, coor_y):
    """Функция, которая рекурсивно, с помощью метода "разделяй и властвуй" находит
    минимальное расстояние между точками"""
    n = len(coor_x)
    if n <= 3:
        return round(min(dist(coor_x[i], coor_x[j]) for i in range(n) for j in range(i + 1, n)), 7)

    mid = n // 2

    left_part_coor_x = coor_x[:mid]
    right_part_coor_x = coor_x[mid:]

    left_part_coor_y = [c for c in coor_y if c[0] <= coor_x[mid][0]]
    right_part_coor_y = [c for c in coor_y if c[0] > coor_x[mid][0]]

    left_dist = recurse(left_part_coor_x, left_part_coor_y)
    right_dist = recurse(right_part_coor_x, right_part_coor_y)

    min_dist = min(left_dist, right_dist)
    string = [c for c in coor_y if abs(c[0] - coor_x[mid][0]) < min_dist]
    if len(string) <= 1:
        return round(min(dist(coor_x[i], coor_x[j]) for i in range(n) for j in range(i + 1, n)), 7)
    return round(min(min_dist, min(dist(string[i], string[j]) for i in range(len(string)) for j in range(i + 1, min(i + 7, len(string))))), 7)


def min_distan(coord):
    """Функция которая сортирует координаты"""
    coor_x = sorted(coord, key=lambda x: x[0])
    coor_y = sorted(coord, key=lambda y: y[1])
    return recurse(coor_x, coor_y)
