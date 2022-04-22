def high_and_low(list1):
    news = []
    list2 = list1.split()

    for i in list2:
        news.append(int(i))

    news.sort()

    hi = str(news[-1])
    lo = str(news[0])
    return hi + " " + lo
