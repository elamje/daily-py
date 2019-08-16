def inter(a,b):
    return a & b # treat each list as a set, intersection of sets

def length(head):
    if not head:
        return 0
    return 1 + length(head.next)

def intersection(a, b):
    x, y = length(a), length(b)
    cur_a, cur_b = a, b

    if x > y:
        for _ in range(x - y):
            cur_a = cur_a.next

    else:
        for _ in range(y-x):
            cur_b = cur_b.next

    while cur_a != cur_b:
        cur_a = cur_a.next
        cur_b = cur_b.next
    return cur_a

def naive(a,b):
    s = set()
    while a.peek() != None:
        s.add(a)
        a = a.next

    while not s.__contains__(b):
        b = b.next

    return b