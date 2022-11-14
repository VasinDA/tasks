# TODO: Coulde we resolve it for O(n)?
# TODO: pelase test with [1,2,31,2]
def couldBeSorted(mylist):
    counter = 0
    len_list = len(mylist)
    # TODO: the condition is wrong, let's check with [6,2,3,4,5,1]
    if min(mylist) == mylist[0] or max(mylist) == mylist[len_list - 1]:
        return beSortedUp(mylist, counter, len_list)
    return beSortedDown(mylist, counter, len_list)

# TODO: let's think about parameters, do we really need of them?
def beSortedUp(mylist, counter, len_list):
    for i in range(len_list):
        lowest_index = i
        if counter > 1:
                return False
        for j in range(i + 1, len_list):
           if mylist[j] < mylist[lowest_index]:
                lowest_index = j
                counter += 1
        mylist[i], mylist[lowest_index] = mylist[lowest_index], mylist[i]
    return True

# TODO: could we have only 1 function for sorting? Maybe with param `direction`...
def beSortedDown(mylist, counter, len_list):
    for i in range(len_list):
        biggest_index = i
        if counter > 1:
                return False
        for j in range(i + 1, len_list):
           if mylist[j] > mylist[biggest_index]:
                biggest_index = j
                counter += 1
        mylist[i], mylist[biggest_index] = mylist[biggest_index], mylist[i]
    return True