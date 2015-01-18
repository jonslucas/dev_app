
def hash(st):
    """
    Base-37 counter. Increments on a 0-15 scale based on letts (below).
    """
    letts = 'acdegilmnoprstuw'
    h = 7
    for i in xrange(len(st)):
        h = (h*37+letts.index((st[i])))
    return h

def machine(targ, str_len=9):
    init = hash('aaaaaaaaa')
    diff = targ-init
    i = str_len - 1 #shift to zero index
    counter =[0 for c in xrange(str_len)]
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
    #Gen_dev
    tar1 = 945924806726376
    #T_dev
    tar2 = 914117715920704
    print parse_to_string(machine(tar1))
    print parse_to_string(machine(tar2))


if __name__ == "__main__":
    main()
        
