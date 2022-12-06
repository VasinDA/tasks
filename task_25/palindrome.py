def palinDrome(str):
    if not str:
        return False
    if str.isdigit():
        return False
    if len(str) == 1:
        return True
    str_list = list(str)
    len_str_list_half = len(str_list) // 2
    counter =  len_str_list_half
    for idx in range(len_str_list_half):
        if str_list[idx].isdigit():
            # TODO: may we eleminate the `del` amd ise L- and R- pointers?
            del str_list[idx]
            palinDrome(''.join(str_list))
        if str_list[-idx - 1].isdigit():
            del str_list[-idx - 1]
            palinDrome(''.join(str_list))
        if str_list[idx].lower() == str_list[-idx - 1].lower():
            counter -= 1
    return counter == 0



