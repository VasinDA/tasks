def hintCounter(list):
    dict = {}
    for i in list:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1
    list = []
    for key in dict:
        hint = dict[key] // 2
        if hint > 0:
            for _ in range(hint):
                pair_list = [key for _ in range(2)]
                list.append(pair_list)
    return list
         
    
