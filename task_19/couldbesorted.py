#def couldBeSorted(mylist):



def swapCounter(mylist):
    swap_dict = {'>':0, '<':0, 'swap_up':[], 'swap_down':[]}
    for index in range(len(mylist)-1):
        value = mylist[index]
        next_value = mylist[index + 1]
        if value < next_value:
            swap_dict['swap_up'].append(index)
            swap_dict['>'] += 1
        if value > next_value:
            swap_dict['swap_down'].append(index + 1)
            swap_dict['<'] += 1
    return swap_dict 

mylist = [6,2,3,4,5,1]
print(swapCounter(mylist))