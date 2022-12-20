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
    # That works, but I'd like to see solution just with one `for`.
    for _ in range(len_str):
        if str[start].isdigit():
            start += 1
            continue
        if str[end].isdigit():
            end -= 1
            continue
        if str[start].lower() != str[end].lower():
            return False
        start += 1
        end -= 1
    return True


