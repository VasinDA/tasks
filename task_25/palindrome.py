def palinDrome(str):
    if not str:
        return False
    if str.isdigit():
        return False
    len_str = len(str)
    if len_str == 0:
        return True
    start = 0 
    end = len_str - 1
    while start < end:
        while str[start].isdigit():
            start += 1
        while str[end].isdigit():
            end -= 1
        if str[start].lower() != str[end].lower():
            return False
        start += 1
        end -= 1
    return True


