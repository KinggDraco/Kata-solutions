def move_zeros(array):
    zeros = 0 
    new = []
    for x in array:
        if x != 0:
            new.append(x)
        else: zeros += 1

    while zeros >= 1:
            new.append(0)
            zeros -= 1
    return new
