import random
from prettytable import PrettyTable

from heap_sort import heap_sort
from smooth_sort import smooth_sort
from beenary_tree_sort import beenary_tree_sort

algorithms = (
    ("heap_sort", heap_sort),
    ("smooth_sort", smooth_sort),
    ("beenary_tree_sort", beenary_tree_sort)
)

if __name__ == "__main__":
    for i in range(25):
        print(f"ARRAY LEN: {i}")
        tbl = PrettyTable()
        tbl.field_names = ["name", "status"]
        arr = list(range(i))
        random.shuffle(arr)
        for name, fun in algorithms:
            random.shuffle(arr)
            verdict = "SUCCESS" if list(range(i)) == fun(arr) else "FAILURE"
            tbl.add_row([name, verdict])
        print(tbl)