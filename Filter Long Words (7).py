def filter_long_words(sentence, n):
    list_of_words = sentence.split(' ')
    ret = []
    for x in list_of_words:
        if len(x) > n:
            ret.append(x)
    return ret
