def sumOfTwo(mylist, sum):
    mydict = {}
    for index in range(len(mylist)):
        value = sum - mylist[index]
        if value in mydict:
            return [mydict[value], index]
        mydict[value] = index


