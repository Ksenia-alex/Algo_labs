import tracemalloc
import time
from lab5.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def heapify_up(heap: list, index: int) -> None:
    """
    Процедура для восстановления свойств кучи(вверх)
    :param heap: list
    :param index: int
    :return: None
    """
    while index > 0:
        parent = (index - 1) // 2
        if heap[index] < heap[parent]:
            heap[index], heap[parent] = heap[parent], heap[index]
            index = parent
        else:
            break


def heapify_down(heap: list, index: int) -> None:
    """
    Процедура для восстановления свойств кучи(вниз)
    :param heap: list
    :param index: int
    :return: None
    """
    size = len(heap)
    while index < size:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < size and heap[left] < heap[smallest]:
            smallest = left
        if right < size and heap[right] < heap[smallest]:
            smallest = right
        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            index = smallest
        else:
            break


def add(heap: list, value: int) -> None:
    """
    Добавление элемента в кучу
    :param heap: list
    :param value: int
    :return: None
    """
    heap.append(value)
    heapify_up(heap, len(heap) - 1)


def extract_min(heap: list, removed: set):
    """
    Извлечение минимального элемента из кучи
    :param heap: list
    :param removed: set
    """
    if len(heap) == 0:
        return "*"
    min_elem = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    heapify_down(heap, 0)

    while min_elem in removed:
        if len(heap) == 0:
            return "*"
        min_elem = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        heapify_down(heap, 0)
    return min_elem


def decrease(heap: list, insertion_order: list, index: int, new_value: int, removed: set) -> None:
    """
    Уменьшение элемента в куче
    :param heap: list
    :param insertion_order: list
    :param index: int
    :param new_value: int
    :param removed: set
    :return: None
    """
    old_value = insertion_order[index]
    if old_value > new_value:
        removed.add(old_value)
        add(heap, new_value)
        insertion_order[index] = new_value


def process_operations(n, operations):
    heap = []
    insertion_order = []
    removed = set()
    results = []

    for i in range(n):
        operation = operations[i].split()
        if operation[0] == "A":
            add(heap, int(operation[1]))
            insertion_order.append(int(operation[1]))
        elif operation[0] == "X":
            result = extract_min(heap, removed)
            results.append(str(result))
        elif operation[0] == "D":
            idx = int(operation[1]) - 1
            new_value = int(operation[2])
            decrease(heap, insertion_order, idx, new_value, removed)

    return results


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    n = int(lines[0])
    operations = [i.strip() for i in lines[1:]]
    if 1 <= n <= 10 ** 6:
        result = results = process_operations(n, operations)
        write_file('\n'.join(map(str, result)), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()
