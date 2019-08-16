# depends on inputs being sorted currently

def scheduler(time):
    #greedy
    n = len(time)
    array = [(0,0)] * n
    for t in time:
        #while no overlap with array elements
        for i in range(n):
            if (array[i][1] <= t[0]):
                array[i] = t
                break
    return sum(map(lambda i: 1 if i!=(0,0) else 0, array ))

scheduler([(30,50),(0,29),(60,150)])