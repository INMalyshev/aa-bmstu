import random
from time import time
from prettytable import PrettyTable

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

        for i in range(1, 202, 25):
            row = [i]

            t1 = time()
            for _ in range(N):
                arr = list(range(i))
                fun(arr)
            t2 = time()
            row.append(round((t2-t1)/N*MICRO, 3))

            t1 = time()
            for _ in range(N):
                arr = list(range(i))
                arr.reverse()
                fun(arr)
            t2 = time()
            row.append(round((t2-t1)/N*MICRO, 3))

            t1 = time()
            for _ in range(N):
                arr = list(range(i))
                random.shuffle(arr)
                fun(arr)
            t2 = time()
            row.append(round((t2-t1)/N*MICRO, 3))

            tbl.add_row(row)

        print(name)
        print(tbl)
