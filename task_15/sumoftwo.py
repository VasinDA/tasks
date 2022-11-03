def sumOfTwo(mylist, sum):
    mydict = {}
    result_list = []
    for index in range(len(mylist)):
        value = sum - mylist[index]
        if value in mydict:
            result_list.append(mydict[value])
        mydict[value] = index
    return result_list

