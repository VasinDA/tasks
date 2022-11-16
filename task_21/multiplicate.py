#solution 1
def multiplicationSol1(a,b):
    c = abs(a)
    d = abs(b)
    multi = c
    for _ in range(d-1):
        multi += c
    if a < 0 or b < 0:
        return -multi
    return multi

#solution 2
def multiplicationSol2(a, b):
    c = abs(a)
    d = abs(b)
    mylist = [c for _ in range(d)]
    if a< 0 or b < 0:
        return -sum(mylist)
    return sum(mylist)   

#solution 3
def multiplicationSol3(a, b):
    c = abs(a)
    d = abs(b)
    mylist = []
    if a < 0 or b < 0:
        return -sum(recorsion(c, d, mylist))
    return sum(recorsion(c, d, mylist))

def recorsion(c, d, mylist):
    if d == 0:
        return mylist
    mylist.append(c)
    return recorsion(c, d-1, mylist)


a, b = 2,3
print(multiplicationSol3(a,b))