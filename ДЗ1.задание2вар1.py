def sumbilet(chislo_v_bilete):
    summa = 0
    while chislo_v_bilete:
        summa = summa + (chislo_v_bilete % 10)
        chislo_v_bilete = chislo_v_bilete // 10
    return summa


for i in range(0,1000000,1):
    # print(i)
    if sumbilet(i)%7 == 0:
        print(str(i) + " счастливый билет")





