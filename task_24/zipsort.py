def zipSort(arr1, arr2):
    if not arr1 and not arr2:
        return []
    new_arr = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            new_arr.append(arr1[0])
            del arr1[0]
        elif arr1[0] > arr2[0]:
            new_arr.append(arr2[0])
            del arr2[0]
    if arr1:
        new_arr = new_arr + arr1
    new_arr = new_arr + arr2
    return new_arr
