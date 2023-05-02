def f(n):
    stroka=bin(n)[2:]
    stroka+=stroka[-2:]
    return int(stroka,2)
for i in range(10000):
    if f(i)>100:
        print(i)
        break