def delDuplicate(mylist):
    mydict = {}
    newlist = []
    for i in mylist:
        if i not in mydict:
            newlist.append(i)
        mydict[i] = 0
    return newlist
        
