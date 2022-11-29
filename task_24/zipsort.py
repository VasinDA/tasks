def zipSort(arr1, arr2):
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    new_arr = []
    while arr1 and arr2:
       
            if arr1[0] < arr2[0]:
                new_arr.append(arr1[0])
                del arr1[0]
                len_arr1 -= 1
            elif arr1[0] > arr2[0]:
                new_arr.append(arr2[0])
                del arr2[0]
                len_arr2 -= 1
    if len_arr1 == 0:
        new_arr = new_arr + arr2
    new_arr = new_arr + arr1
            
    return new_arr

arr1 = [3,5]
arr2 = [1,2,4]
print(zipSort(arr1, arr2))