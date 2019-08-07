import pdb


def xor(x,y):
    return ((x | y) & ~(x & y))

# root and tail are edge cases
# node 1 @ addr:1 | both = 1 
# node 2 @ addr:2 | both = 2
# node 6 @ addr:3 | both = 7
# node 3 @ addr:5 | both = 5
# you are at root or tail when addr = both
# make everything inside of an array, let index of array be addr

list = []

head = None

def get_pointer(node):
    return node.addr

def deref_pointer(mem, addr):
    return mem[addr]

def insert():
    global head, list
    if (head == None): # head is null
        head = XorNode(0,-1,1)
        list.append(head)
        return
    if (len(list) == 1): # list has 1 element
        list.append(XorNode(1,0,0))
        return
    from_addr = 1
    curr = head
    while (curr.both != curr.addr):
        next = xor(from_addr, curr.both) # get next addr
        curr = deref_pointer(list, next)
        from_addr = curr.addr
        pdb.set_trace()
    prev = deref_pointer(list,from_addr)
    prev.both = xor(prev.)
    node_to_add = XorNode(from_addr + 1, from_addr, from_addr + 2)
    list.append(node_to_add)
    return

class XorNode:
    addr = 0 # only stored bc python doesn't have pointers
    both = 0

    def __init__(self, addr, prev, next):
        self.both = xor(prev, next)
        self.addr = addr

    def get_next(self,from_addr):
        return xor(self.both,from_addr) #if self.both != self.addr else "{} {}".format(xor(self.both,from_addr), "TAIL")

    def get_prev(self, from_addr):
        return xor(self.both,from_addr) #if self.both != self.addr else "{} {}".format(xor(self.both, from_addr), "HEAD")

    def __str__(self):
        return "[addr: {} | both: {}]".format(self.addr, self.both)
        
        

# solution

import ctypes


# This is hacky. It's a data structure for C, not python.
class Node(object):
    def __init__(self, val):
        self.val = val
        self.both = 0


class XorLinkedList(object):
    def __init__(self):
        self.head = self.tail = None
        self.__nodes = [] # This is to prevent garbage collection

    def add(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.both = id(node) ^ self.tail.both
            node.both = id(self.tail)
            self.tail = node

        # Without this line, Python thinks there is no way to reach nodes between
        # head and tail.
        self.__nodes.append(node)


    def get(self, index):
        prev_id = 0
        node = self.head
        for i in range(index):
            next_id = prev_id ^ node.both

            if next_id:
                prev_id = id(node)
                node = _get_obj(next_id)
            else:
                raise IndexError('Linked list index out of range')
        return node


def _get_obj(id):
    return ctypes.cast(id, ctypes.py_object).value
