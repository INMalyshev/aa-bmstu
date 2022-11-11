from algorithm import *

ALG = [
    non_recursive_levenshtein,
    non_recursive_damerau_levenshtein,
    recursive_damerau_levenshtein,
    recursive_damerau_levenshtein_with_cache
]

inp = ('1234', '2143')
for f in ALG:
    print(f(*inp))