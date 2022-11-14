def couldBeSorted(mylist):
    if len(mylist) <= 2:
        return False
    mydict = swapToSorted(mylist)
    
    if mydict['<'] == 0 or mydict['>'] == 0:
        return False
    if mydict['<'] == 1 or mydict['>'] == 1:
        return True
    return False


def swapToSorted(mylist):
    swap_dict = {'>':0, '<':0}
    for index in range(len(mylist)-1):
        value = mylist[index]
        next_value = mylist[index + 1]
        if next_value > value:
            swap_dict['>'] += 1
        if next_value < value:
            swap_dict['<'] += 1
    
    return swap_dict

mylist = [1,4,2,3] 
print(swapToSorted(mylist))