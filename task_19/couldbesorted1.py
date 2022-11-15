def couldBeSorted(mylist):
    counter = 0
    len_list = len(mylist)
    if min(mylist) == mylist[0] or max(mylist) == mylist[len_list - 1]:
        return beSortedUp(mylist, counter, len_list)
    return beSortedDown(mylist, counter, len_list)

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

mylist = [6,2,3,4,5,1]
print(couldBeSorted(mylist))