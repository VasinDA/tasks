def zipSort(arr1, arr2):
    if not arr1 and not arr2:
        return []
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    index_arr1 = 0
    index_arr2 = 0
    new_arr = []
    while index_arr1 < arr1_len and index_arr2 < arr2_len:
        # TODO: both `while` llops look similar, can we make that code common?
        while arr1[index_arr1] < arr2[index_arr2]:
            appendNewArrValue(arr1, new_arr, index_arr1)
        while arr2[index_arr2] < arr1[index_arr1]:
            appendNewArrValue(arr2, new_arr, index_arr2)
    if index_arr1 < arr1_len:
        new_arr = new_arr + arr1[index_arr1:]
    new_arr = new_arr + arr2[index_arr2:]
    return new_arr

def appendNewArrValue(arr, new_arr, index):
    new_arr.append[arr[index]]
    index += 1 
    return index