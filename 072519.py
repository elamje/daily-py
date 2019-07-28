import numpy as np
vec = [1, 2, 3, 4, 5]

#brute force pass, then divide
#special case if 0 in array
def allxi(vec):
    tot = 1;
    res = range(len(vec));
    for x in vec:
        if (x == 0):
            return np.zeros(len(vec))
        tot *= x
    for i in range(len(vec)):
        res[i] = tot / vec[i]
    return res

#if you can't divide, you must use O(N) time and space
# [element_i] is product of numbers before i and numbers after i
# O(N) to generate prefix products, O(n) to generate suffix
#    vec = [1, 2, 3, 4]
# prefix = [1, 1, 2, 6]
# suffix = [24, 12, 4, 1]
# result = prefixi * suffixi

