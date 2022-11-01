def sumSimilar(list):
    dict = {}
    for i in list:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1
    sum = 0
    for key in dict:
        if dict[key] > 2:
            sum += key * dict[key]
    return sum
