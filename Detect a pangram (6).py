import string

def is_pangram(s):
    s = s.lower()
    letter_list = []

    for i in s:
        if i not in letter_list and i.isalpha():
            letter_list.append(i)

    letter_list.sort()
    new_list = list(string.ascii_lowercase)
    
    print(letter_list, new_list)
    if letter_list == new_list:
        return True
    
    return False

s = ""
is_pangram(s)
