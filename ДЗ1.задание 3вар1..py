import random
n = int(input("введите размер списка:\n"))
A = []
for i in range(n):
    a = int(random.random()*100)
    A.append(a)
print(A)
chislo = int(input("введите число для удаления из списка:\n"))
A.pop(chislo)
print(A)