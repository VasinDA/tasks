from math import log, ceil

def numQuest():
    upper_limit = int(input('Enter upper limit: '))
    list_for_quest = [i for i in range(1, upper_limit + 1)]
    low = 0
    high = upper_limit - 1
    # TODO: please check for upper boundry = 10, and number = 7
    try_count = ceil(log(upper_limit, 2))
    counter = 0
    print(f'I will guess in {try_count} attempts')
    return searchForSolutionTheQuest(list_for_quest, low, high, counter)

def searchForSolutionTheQuest(list_for_quest, low, high, counter):
    if high >= low:
        counter += 1
        mid = (high + low) // 2
        print(list_for_quest[mid])
        question = input('If the number is less than the specified - "less" \nIf the number is greater than the specified - "more" \nIf guessed - "yes" \n')
        if question.lower() == 'yes':
            # TODO: please check for upper boundry = 10, and number = 7
            return counter
        elif question.lower() == 'less':
            return searchForSolutionTheQuest(list_for_quest, low, mid - 1, counter)
        elif question.lower() == 'more':
            return searchForSolutionTheQuest(list_for_quest, mid + 1, high, counter)
        else:
            return searchForSolutionTheQuest(list_for_quest, low, high, counter)


print(numQuest())