def delDuplicate(mylist):
    mydict = {}
    newlist = []
    for i in mylist:
        if i not in mydict:
            newlist.append(i)
            print(newlist)
        mydict[i] = 0
    return newlist
        
