n = int(input('Введите кол-во отрезков: '))
a = int(input('Введите начальное значение:'))
b = int(input('Введите конечное значение:'))
def fyn(ix):
    return 7 / (x ** 2 + 1)
h = (b - a) / n
integ = 0
for i in range(0, n + 1):
    x = a + i * h
    if i != n and i != 0:
        integ += fyn(x)
    if i == 0:
        buf = fyn(x)
    if i == n:
        integ *= 2
        integ += fyn(x)
integ += buf
integ *= h / 2
print('Значение интеграла =', "{0:<14.9g}".format(integ))
