from time import time
from utils import generate_random_string
from algorithm import *

CICLE_COUNT = 10000
MICRO = 1000000

def time_non_recursive_levenshtein(len1, len2, n = CICLE_COUNT):
    inp_datas = [(generate_random_string(len1), generate_random_string(len2)) for i in range(n)]

    t1 = time()
    for inp_data in inp_datas:
        non_recursive_levenshtein(*inp_data)
    t2 = time()
    
    return (t2 - t1) / n * MICRO

def time_non_recursive_damerau_levenshtein(len1, len2, n = CICLE_COUNT):
    inp_datas = [(generate_random_string(len1), generate_random_string(len2)) for i in range(n)]

    t1 = time()
    for inp_data in inp_datas:
        non_recursive_damerau_levenshtein(*inp_data)
    t2 = time()
    
    return (t2 - t1) / n * MICRO

def time_recursive_damerau_levenshtein(len1, len2, n = CICLE_COUNT):
    inp_datas = [(generate_random_string(len1), generate_random_string(len2), len1, len2) for i in range(n)]

    t1 = time()
    for inp_data in inp_datas:
        recursive_damerau_levenshtein(*inp_data)
    t2 = time()
    
    return (t2 - t1) / n * MICRO

def time_recursive_damerau_levenshtein_with_cache(len1, len2, n = CICLE_COUNT):
    inp_datas = [(generate_random_string(len1), generate_random_string(len2), len1, len2, [[-1 for _ in range(len1 + 1)] \
        for __ in range(len2 + 1)]) for i in range(n)]

    t1 = time()
    for inp_data in inp_datas:
        recursive_damerau_levenshtein_with_cache(*inp_data)
    t2 = time()
    
    return (t2 - t1) / n * MICRO

SECTIONS = (
    (time_non_recursive_levenshtein, 'NON RECURSIVE LEVENSHTEIN'),
    (time_non_recursive_damerau_levenshtein, 'NON RECURSIVE DAMERAU LEVENSHTEIN'),
    (time_recursive_damerau_levenshtein_with_cache, 'RECURSIVE DAMERAU LEVENSHTEIN WITH CACHE'),
    (time_recursive_damerau_levenshtein, 'RECURSIVE DAMERAU LEVENSHTEIN')
)

TESTS = (
    (0, 0),
    (1, 1),
    (3, 3),
    (5, 5),
    (10, 10),
    (25, 25)
)

OUTPUT_FILE = 'timing.txt'

if __name__ == '__main__':
    with open(OUTPUT_FILE, 'wt') as f:
        for section in SECTIONS:
            fun, title = section
            print(title)
            f.write(f'{title}\n')
            
            for test in TESTS:
                timing = int(fun(*test))
                print(f'{test[0]} : {test[1]} -> {timing} microseconds')
                f.write(f'{test[0]} {test[1]} {timing}\n')