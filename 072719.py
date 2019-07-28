list = [3, 4, -1, 1]
list2 = [1, 2, 0]

# runs in O(N) time and space, so breaks constant space req
def lowpos(d):
    #use set since dups don't matter
    d = set(d)
    i = 1
    while i in d:
        i += 1
    return i

# runs in O(N) time, O(1) space
# a different trick:
# use the index of the array to store values
# the only nums relevant to solution are positive numbers less than len(array)
# fortunately the array has indices that match this constraint
# iterate array: throwaway negatives and numbers bigger than array length, move positives to their index
#iterate array again: look for when index != val @ index, return index as result

