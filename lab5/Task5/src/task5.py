import tracemalloc
import time
from lab5.utils import *

t_start = time.perf_counter()
tracemalloc.start()


def parallel_task_processing(count_threads: int, count_task: int, times: list[int]) -> list[tuple]:
    """
    функция для работы с планировщиком заданий
    :param count_threads: int
    :param count_task: int
    :param times: list[int]
    :return: list[tuple]
    """
    free_threads = [(0, i) for i in range(count_threads)]
    result = []
    for t in range(count_task):
        task_time = times[t]
        free_threads.sort()
        free_time, thread_id = free_threads.pop(0)
        start_time = free_time
        end_time = start_time + task_time
        free_threads.append((end_time, thread_id))
        result.append((thread_id, start_time))

    return result


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXTF_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "txtf")
INPUT_PATH = os.path.join(TXTF_DIR, "input.txt")
OUTPUT_PATH = os.path.join(TXTF_DIR, "output.txt")

if __name__ == "__main__":
    lines = open_file(INPUT_PATH)
    num, count_task = map(int, lines[0].split())
    times = list(map(int, lines[1].split()))
    if 1 <= int(num) <= 10 ** 5 and 1 <= int(count_task) <= 10 ** 5:
        result = parallel_task_processing(num, count_task, times)
        res = []
        for thread_id, start_time in result:
            res.append(f'{thread_id} {start_time}')
        write_file('\n'.join(res), OUTPUT_PATH)
    else:
        print("Введите корректные данные")

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
    tracemalloc.stop()