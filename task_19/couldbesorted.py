def couldBeSorted(mylist):
    counter = 0
    len_list = len(mylist)
    if min(mylist) == mylist[0] or max(mylist) == mylist[len_list - 1]:
        return beSortedUp(mylist, counter, len_list)
    return beSortedDown(mylist, counter, len_list)

def beSortedUp(mylist, counter, len_list):
    for i in range(len_list):
        smallest_index = i
        for j in range(i + 1, len_list):
            if mylist[j] < mylist[smallest_index]:
                smallest_index = j
        mylist[i], mylist[smallest_index] = mylist[smallest_index], mylist[i]
        counter += 1 
    return counter




mylist = [4,2,3,1]
print(couldBeSorted(mylist))