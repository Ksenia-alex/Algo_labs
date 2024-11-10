def dist(coor1: (float, float)) -> float:
    """Функция для нахождения расстояние между точкой и началом координат"""
    return coor1[0] ** 2 + coor1[1] ** 2


def count(coor: (float, float), k: int) -> [float]:
    """Функция для подсчета количества точек"""
    return [i[1] for i in sorted([(dist(cor), [cor[0], cor[1]]) for cor in coor])[:k]]
