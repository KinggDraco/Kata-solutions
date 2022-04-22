def in_asc_order(arr):
    ranges = len(arr)
    x = 0
    while x < ranges - 1:
        if arr[x] <= arr[x + 1]:
            print("Lower")
            print(x)

        else:
            print("Higher")
            return False

        x += 1
    return True


