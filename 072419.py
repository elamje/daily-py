
list = [10,15,3,7]
k = 17

def addable(list, k):
    for x in list:
        if (x <= k):
            for y in list[list.index(x)+1:]:
                if (k == x + y):
                    return True
    return False
                
# O(N * N/2) = O(N^2)

# in order to speed up, do it in place, remembering the difference in a set(dictionary under the hood)
def add_(list,k):
    sat = set() # gives O(1) lookup bc dict under hood
    for x in list:
        if (x in sat):
            return True
        sat.add(k-x)
    return False

        
