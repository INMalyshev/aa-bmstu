import random
from prettytable import PrettyTable
import tracemalloc

from heap_sort import heap_sort
from smooth_sort import smooth_sort
from beenary_tree_sort import beenary_tree_sort

algorithms = (
    ("Сортировка кучей", heap_sort),
    ("Плавная сортировка", smooth_sort),
    ("Сортировка бинарным деревом", beenary_tree_sort)
)

N = 1000
MICRO = 1000000

if __name__ == "__main__":
    for name, fun in algorithms:
        tbl = PrettyTable()
        tbl.field_names = ["Количество элементов", "Отсортированный массив", "Упорядоченный по убыванию массив", "Не отсортированный массив"]

        for i in range(25):
            row = [i]

            arr = list(range(i))
            tracemalloc.start()
            curr, peak = tracemalloc.get_traced_memory()
            fun(arr)
            curr, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            row.append(peak)

            arr = list(range(i))
            arr.reverse()
            tracemalloc.start()
            curr, peak = tracemalloc.get_traced_memory()
            fun(arr)
            curr, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            row.append(peak)

            arr = list(range(i))
            random.shuffle(arr)
            tracemalloc.start()
            curr, peak = tracemalloc.get_traced_memory()
            fun(arr)
            curr, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            row.append(peak)

            tbl.add_row(row)

        print(name)
        print(tbl)
