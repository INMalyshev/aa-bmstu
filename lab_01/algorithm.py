def non_recursive_levenshtein(s1, s2):
    distances = [[0 for _ in range(len(s1) + 1)] for __ in range(len(s2) + 1)]

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            cur_dist = -1
            if i == 0 and j == 0:
                cur_dist = 0
            elif i == 0 and j > 0:
                cur_dist = j
            elif j == 0 and i > 0:
                cur_dist = i
            else:
                left = distances[j][i - 1] + 1
                up = distances[j - 1][i] + 1
                left_up = distances[j - 1][i - 1] + (0 if s1[i - 1] == s2[j - 1] else 1)
                cur_dist = min(left, up, left_up)
            
            distances[j][i] = cur_dist

    return distances[len(s2)][len(s1)]

def non_recursive_damerau_levenshtein(s1, s2):
    distances = [[0 for _ in range(len(s1) + 1)] for __ in range(len(s2) + 1)]

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            cur_dist = -1
            if i == 0 and j == 0:
                cur_dist = 0
            elif i == 0 and j > 0:
                cur_dist = j
            elif j == 0 and i > 0:
                cur_dist = i
            else:
                left = distances[j][i - 1] + 1
                up = distances[j - 1][i] + 1
                left_up = distances[j - 1][i - 1] + (0 if s1[i - 1] == s2[j - 1] else 1)
                if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                    exchange = distances[j - 2][i - 2] + 1
                    cur_dist = min(left, up, left_up, exchange)
                else:
                    cur_dist = min(left, up, left_up)
                
            distances[j][i] = cur_dist

    return distances[len(s2)][len(s1)]

def recursive_damerau_levenshtein(s1, s2, i, j):
    if i == 0 and j == 0:
        return 0
    elif i == 0 and j > 0:
        return j
    elif j == 0 and i > 0:
        return i
    else:
        left = recursive_damerau_levenshtein(s1, s2, i - 1, j) + 1
        up = recursive_damerau_levenshtein(s1, s2, i, j - 1) + 1
        left_up = recursive_damerau_levenshtein(s1, s2, i - 1, j - 1) + (0 if s1[i - 1] == s2[j - 1] else 1)
        if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
            exchange = recursive_damerau_levenshtein(s1, s2, i - 2, j - 2) + 1 if (i > 0 and j > 0 \
                and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]) else left_up
            return min(left, up, left_up, exchange)
        else:
            return min(left, up, left_up)

def recursive_damerau_levenshtein_with_cache(s1, s2, i, j, cache):
    if cache[j][i] != -1:
        return cache[j][i]
    
    if i == 0 and j == 0:
        cache[j][i] = 0
        return cache[j][i]
    elif i == 0 and j > 0:
        cache[j][i] = j
        return cache[j][i]
    elif j == 0 and i > 0:
        cache[j][i] = i
        return cache[j][i]
    else:
        left = recursive_damerau_levenshtein_with_cache(s1, s2, i - 1, j, cache) + 1
        up = recursive_damerau_levenshtein_with_cache(s1, s2, i, j - 1, cache) + 1
        left_up = recursive_damerau_levenshtein_with_cache(s1, s2, i - 1, j - 1, cache)\
            + (0 if s1[i - 1] == s2[j - 1] else 1)
        if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
            exchange = recursive_damerau_levenshtein_with_cache(s1, s2, i - 2, j - 2, cache)\
                + 1 if (i > 0 and j > 0 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]) else left_up
            cache[j][i] = min(left, up, left_up, exchange)
        else:
            cache[j][i] = min(left, up, left_up)
        
        return cache[j][i]
