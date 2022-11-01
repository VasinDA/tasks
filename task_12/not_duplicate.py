def notDuplicate(list):
    dict = {}
    for i in list:
        if i not in dict:
            dict[i] = 0
        dict[i] +=1
    list = [key for key in dict if dict[key] == 1]
    return list
