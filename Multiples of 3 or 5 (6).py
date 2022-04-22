def solution(number):
    i=1
    numbas = []
    while i < number:
        if i % 3 == 0 and i not in numbas:
            numbas.append(i)
        if i % 5 == 0 and i not in numbas:
            numbas.append(i)
        i+=1
    return sum(numbas)
