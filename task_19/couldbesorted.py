def couldBeSorted(mylist):
    len_list = len(mylist)
    if len_list <= 2:
        return False
    swap_dict = {'>':0, '<':0}
    for index in range(1, len_list):
        value = mylist[index - 1]
        next_value = mylist[index]
        if next_value > value:
            swap_dict['>'] += 1
        if next_value < value:
            swap_dict['<'] += 1
    if swap_dict['>'] == 0 or swap_dict['<'] == 0:
        return False
    if swap_dict['>'] >= swap_dict['<']:
        return beSortOneSwap(mylist)
    mylist = mylist[::-1]
    return beSortOneSwap(mylist)

def beSortOneSwap(mylist):
    len_list = len(mylist)
    first_value, second_value = 0, 0
    counter = 0
    for index in range(len_list):
        if mylist[index] < mylist[index - 1]:
            counter += 1
            if first_value == 0:
                first_value = index
            else:
                second_value = index
    if counter > 2:
        return False
    if counter == 2 and len_list > 4:
        mylist[first_value - 1], mylist[second_value] = mylist[second_value], mylist[first_value - 1]
    else:    
        mylist[first_value - 1], mylist[first_value] =  mylist[first_value], mylist[first_value - 1]
    for index in range(1, len_list):
        if mylist[index] < mylist[index -1]:
            return False
    return True