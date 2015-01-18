import itertools


def hash(st):
    """
    Base-37 counter. Increments on a 0-15 scale based on letts (below).
    (base_scale) + (x*37**n), where base_scale is derived from the letter position
    in the 'letts' string and x is the number of times that base has incremented.
    """
    letts = 'acdegilmnoprstuw'
    h = 7
    for i in xrange(len(st)):
        h = (h*37+letts.index((st[i])))
    return h

def machine():
    targ = 945924806726376
    init = hash('aaaaaaaaa')
    diff = targ-init
    i = 8
    counter =[0,0,0,0,0,0,0,0,0]
    while i >= 0:
        x = diff/37**i
        counter[i]=x
        diff -=((37**i)*x)
        i -=1
    return counter

def parse_to_string(c):
    """
    Takes counter number values (c) and turns them back into the string values
    determined by the provided string.
    """
    letts = 'acdegilmnoprstuw'
    return ''.join([letts[i] for i in c[::-1]])

def main():
    print parse_to_string(machine())


if __name__ == "__main__":
    main()
        
