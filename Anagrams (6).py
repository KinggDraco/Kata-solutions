def anagrams(inputs, lists):
    foo1 = sorted(inputs)
    foo2 = lists
    foo3 = []

    for y in foo2:
        print(sorted(y))
        if sorted(y) == foo1:
            foo3.append(y)
    return foo3


