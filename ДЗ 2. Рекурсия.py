a = int(input('Введите сторону прямоугольника a:\n'))
b = int(input('Введите сторону прямоугольника b:\n'))
A = []

def rec(a, b):
    if a > b:
        return rec(a - b, b) + rec(b, b)
    elif a < b:
        return rec(a, b - a) + rec(a, a)
    elif a == b:
        A.append(a)
        return 1

A.sort(reverse=True)
A = [str(a) + 'X' + str(a) for a in A]
print('Количество вырезанных квадратов:', rec(a, b))
print('Все вырезанные квадраты:', A)