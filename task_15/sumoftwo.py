def sumOfTwo(mylist, sum):
    mydict = {}
    for index in range(len(mylist)):
        value = sum - mylist[index]
        if mylist[index] in mydict:
            return [mydict[mylist[index]], index]
        mydict[value] = index
        
