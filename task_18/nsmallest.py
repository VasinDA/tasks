def nSmallest(list_of_chmob, n):
    for i in range(n):
        smallest_index = i
        for j in range(i + 1, len(list_of_chmob)):
            if list_of_chmob[j]['price'] < list_of_chmob[smallest_index]['price']:
                smallest_index = j
        list_of_chmob[i], list_of_chmob[smallest_index] = list_of_chmob[smallest_index], list_of_chmob[i]
    return list_of_chmob[:n]

list_of_chmob =  [{'name': 'Ivan', 'price': 2000}, {'name': 'Peter', 'price': 1200}, {'name': 'Ihor', 'price': 2700}, {'name': 'Gregory', 'price': 2500}]
n = 2
print(nSmallest(list_of_chmob, n))