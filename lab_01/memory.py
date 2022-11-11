import tracemalloc
from utils import generate_random_string
from algorithm import *

def memory_non_recursive_levenshtein(len1, len2):
    inp_data = (generate_random_string(len1), generate_random_string(len2))

    tracemalloc.start()
    non_recursive_levenshtein(*inp_data)
    curr, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return peak if len1 != 0 else peak - curr

def memory_non_recursive_damerau_levenshtein(len1, len2):
    inp_data = (generate_random_string(len1), generate_random_string(len2))

    tracemalloc.start()
    non_recursive_damerau_levenshtein(*inp_data)
    curr, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return peak if len1 != 0 else peak - curr

def memory_recursive_damerau_levenshtein(len1, len2, n = 10):
    inp_data = (generate_random_string(len1), generate_random_string(len2), len1, len2)

    tracemalloc.start()
    recursive_damerau_levenshtein(*inp_data)
    curr, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return peak if len1 != 0 else peak - curr

def memory_recursive_damerau_levenshtein_with_cache(len1, len2):
    inp_data = (generate_random_string(len1), generate_random_string(len2), len1, len2, \
        [[-1 for _ in range(len1 + 1)] for __ in range(len2 + 1)])

    tracemalloc.start()
    recursive_damerau_levenshtein_with_cache(*inp_data)
    curr, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return peak if len1 != 0 else peak - curr

SECTIONS = (
    (memory_non_recursive_levenshtein, 'NON RECURSIVE LEVENSHTEIN'),
    (memory_non_recursive_damerau_levenshtein, 'NON RECURSIVE DAMERAU LEVENSHTEIN'),
    (memory_recursive_damerau_levenshtein_with_cache, 'RECURSIVE DAMERAU LEVENSHTEIN WITH CACHE'),
    (memory_recursive_damerau_levenshtein, 'RECURSIVE DAMERAU LEVENSHTEIN')
)

TESTS = (
    (0, 0),
    (1, 1),
    (3, 3),
    (5, 5),
    (10, 10),
    (25, 25)
)

OUTPUT_FILE = 'memory.txt'

if __name__ == '__main__':
    with open(OUTPUT_FILE, 'wt') as f:
        for section in SECTIONS:
            fun, title = section
            print(title)
            f.write(f'{title}\n')
            
            for test in TESTS:
                if fun == memory_recursive_damerau_levenshtein and test[0] == 25:
                    continue

                memory = fun(*test)
                print(f'{test[0]} : {test[1]} -> {memory} bytes')
                f.write(f'{test[0]} {test[1]} {memory}\n')