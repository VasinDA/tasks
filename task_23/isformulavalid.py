def isFormulaValid(formula):
    if len(formula) == 0:
        return True
    if len(formula) == 1:
        return False
    if formula[0] == ')':
        return False
    counter = 0
    for i in formula:
        if counter < 0:
            return False
        if i == '(':
            counter += 1
        if i == ')':
            counter -= 1
    if counter == 0:
        return True
    return False

