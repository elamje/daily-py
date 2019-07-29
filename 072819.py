# given
def cons(a,b):
    def pair(f):
        return f(a, b)
    return pair

# you write car and cdr
def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)
