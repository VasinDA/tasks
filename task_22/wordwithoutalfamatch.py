def wordWithOutAlfaMatches(string):
    if len(string) == 0:
        return []
    if len(string) == 1 and string.isalpha():
        return list(string)
    words_list = string.split()
    new_words_list = []
    for word in words_list:
        wordwithoutalfamatches = ''
        word_lower = word.lower()
        for alfa in word:
            if alfa.isalpha():
                if word_lower.count(alfa.lower()) >= 2:
                    wordwithoutalfamatches = ''
                    break
                wordwithoutalfamatches = wordwithoutalfamatches + alfa
        if len(wordwithoutalfamatches) > 0:
            new_words_list.append(wordwithoutalfamatches)
    return new_words_list

