from math import log

def numQuest(higt_limit):
    upper_limit = int(input('Enter upper limit'))
    flag = True
    list_for_quest = [i for i in range(, upper_limit + 1)]
    low = 0
    high = upper_limit - 1
    mid = (high + low) // 2
    try_count = log(upper_limit)
    counter = 0
    while flag == True:
                