def delDuplicate(mylist):
    mydict = {}
    newlist = []
    for i in mylist:
        if i not in mydict:
            newlist.append(i)
        mydict[i] = 0
    return mylist
        
mylist = [1,2,2,4,3,2,1,5,6]
print(delDuplicate(mylist))