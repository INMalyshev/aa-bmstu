from Levenshtein import distance
from pyxdameraulevenshtein import damerau_levenshtein_distance

from algorithm import *

def test_non_recursive_levenshtein(s1, s2):
    idol = distance(s1, s2)
    result = non_recursive_levenshtein(s1, s2)
    message = 'PASSED' if idol == result else 'FAILED'
    
    return (idol - result, message)

def test_non_recursive_damerau_levenshtein(s1, s2):
    idol = damerau_levenshtein_distance(s1, s2)
    result = non_recursive_damerau_levenshtein(s1, s2)
    message = 'PASSED' if idol == result else 'FAILED'
    
    return (idol - result, message)

def test_recursive_damerau_levenshtein(s1, s2):
    idol = damerau_levenshtein_distance(s1, s2)
    result = recursive_damerau_levenshtein(s1, s2, len(s1), len(s2))
    message = 'PASSED' if idol == result else 'FAILED'
    
    return (idol - result, message)

def test_recursive_damerau_levenshtein_with_cache(s1, s2):
    idol = damerau_levenshtein_distance(s1, s2)
    cache = [[-1 for _ in range(len(s1) + 1)] for __ in range(len(s2) + 1)]
    result = recursive_damerau_levenshtein_with_cache(s1, s2, len(s1), len(s2), cache)
    message = 'PASSED' if idol == result else 'FAILED'
    
    return (idol - result, message)

SECTIONS = (
    (test_non_recursive_levenshtein, 'NON RECURSIVE LEVENSHTEIN'),
    (test_non_recursive_damerau_levenshtein, 'NON RECURSIVE DAMERAU LEVENSHTEIN'),
    (test_recursive_damerau_levenshtein, 'RECURSIVE DAMERAU LEVENSHTEIN'),
    (test_recursive_damerau_levenshtein_with_cache, 'RECURSIVE DAMERAU LEVENSHTEIN WITH CACHE')
)

TESTS = (
    ('', ''),
    ('aaa', 'aaa'),
    ('asd', 'asd'),
    ('', 'asd'),
    ('', 'aaa'),
    ('asd', ''),
    ('aaa', ''),
    ('aaa', 'aaaaa'),
    ('asd', 'asdfg'),
    ('as', 'sa'),
    ('asas', 'sasa'),
    ('asas', 'saas'),
    ('asas', 'saasa')
)

if __name__ == '__main__':
    for section in SECTIONS:
        fun, title = section
        print(title)
        
        for test in TESTS:
            rc, mess = fun(*test)

            if rc != 0:
                print(mess, rc, '<---')
            else:
                print(mess)
