def filter_list(l):
    new_list = []
    for x in l:
        print(x)
        if type(x) == int:
            new_list.append(x)
    return(new_list)
l = []
filter_list(l)
