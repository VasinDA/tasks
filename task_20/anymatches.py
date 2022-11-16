def anyMatches(*tuple_list):
    mydict = {}
    for list_values in tuple_list:
        for i in list_values:
            if i not in mydict:
                mydict[i] = 0
            mydict[i] += 1
    new_list = [key for key in mydict if mydict[key] == len(tuple_list)]
    return new_list