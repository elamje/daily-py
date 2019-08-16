def naive(w, st):
    words = w
    string = st
    result = []
    index = 0

    while index < len(string):      # don't trim string at all (immutable will be reallocated/perf hit)
        i = 1
        while not words.__contains__(string[index:index+i]):
            if index + i >= len(string):
                return None
            i += 1
        words.remove(string[index:index+i])
        result.append(string[index:index+i])
        index += i              # Go past word

    return result
