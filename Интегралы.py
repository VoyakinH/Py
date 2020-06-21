# Воякин Алексей Янович ИУ7-14б
# Интегралы


# Ввод данных и задание функции
from math import sin
a = int(input('Введите начальное значение: '))
b = int(input('Введите конечное значение: '))
n1 = 1
n2 = 1
while n1 % 2 == 1:
    n1 = int(input('Введите кол-во частей разбиения (1): '))
    if n1 % 2 == 1:
        print('Кол-во отрезков разбиения должно быть чётным')
while n2 % 2 == 1:
    n2 = int(input('Введите кол-во частей разбиения (2): '))
    if n2 % 2 == 1:
        print('Кол-во отрезков разбиения должно быть чётным')
eps = float(input('Введите степень точности:'))


# Функция
def fyn(ix):
    return ix ** 2
# Первообразная
def per(ix):
    return (ix ** 3) / 3

# Метод правых прямоугольников
h1 = (b - a) / n1
h2 = (b - a) / n2
n = n1
for k in range(0, 2):
    integ = 0
    for i in range(1, n + 1):
        x = (i - 0.5) * h1 + a
        y = fyn(x)
        integ += y
    integ *= h1
    if k == 0:
        inp1 = integ
    else:
        inp2 = integ
    n = n2
    h1 = h2


# Метод парабол
h1 = (b - a) / n1
h2 = (b - a) / n2
n = n1
for k in range(0, 2):
    integ = -1
    ko1 = 0
    ko2 = 0
    for i in range(0, n + 1):
        x = i * h1 + a
        y = fyn(x)
        if integ == -1:
            integ = y
        elif i % 2 == 1:
            ko1 += y
        elif i == n:
            integ += y
        else:
            ko2 += y
    if k == 0:
        ins1 = (h1 / 3) * (integ + (4 * ko1) + (2 * ko2))
    else:
        ins2 = (h1 / 3) * (integ + (4 * ko1) + (2 * ko2))
    h1 = h2
    n = n2


# Вывод таблицы значений
print("Кол-во отрезков|", "Прав. прямоуг. |", " Мет. парабол  |")
print("{0:<14.6g}".format(n1), "|", "{0:<14.6g}".format(inp1), "|", "{0:<14.6g}".format(ins1), "|")
print("{0:<14.6g}".format(n2), "|", "{0:<14.6g}".format(inp2), "|", "{0:<14.6g}".format(ins2), "|")

# Вычисление точного интеграла
toch = per(b) - per(a)
# Вычисление интграла с точностью
print()
if n1 > n2:
    if abs(toch - inp1) > abs(toch - ins1):
        print('Метод правых прямоугольников менее точный')
        p = 1
    else:
        print('Метод Симпсона менее точный')
        p = 0
else:
    if abs(toch - inp2) > abs(toch - ins2):
        print('Метод правых прямоугольников менее точный')
        p = 1
    else:
        print('Метод Симпсона менее точный')
        p = 0
print()
n = 1
if p == 1:
    while abs(inp2 - inp1) > eps:
        integ = 0
        n += 1
        h1 = (b - a) / (2 * n)
        for i in range(1, 2 * n + 1):
            x = (i - 0.5) * h1 + a
            y = fyn(x)
            integ += y
        integ *= h1
        inp1 = integ
        integ = 0
        h1 = (b - a) / n
        for i in range(1, n + 1):
            x = (i - 0.5) * h1 + a
            y = fyn(x)
            integ += y
        integ *= h1
        inp2 = integ
    print('Интеграл вычисленный с заданной точностью =', "{0:<14.9g}".format(inp1))
    print('Абсолютная ошибка =', "{0:<14.9g}".format(abs(toch - inp1)))
    print('Относительная ошибка =', "{0:<14.9g}".format(abs((toch - inp1)/toch)))
else:
    n = 1
    while abs(ins2 - ins1) > eps:
        integ = -1
        n += 1
        h1 = (b - a) / (2 * n)
        ko1 = 0
        ko2 = 0
        for i in range(0, 2 * n + 1):
            x = i * h1 + a
            y = fyn(x)
            if integ == -1:
                integ = y
            elif i % 2 == 1:
                ko1 += y
            elif i == n:
                integ += y
            else:
                ko2 += y
        ins1 = (h1 / 3) * (integ + (4 * ko1) + (2 * ko2))
        integ = -1
        ko1 = 0
        ko2 = 0
        h1 = (b - a) / n
        for i in range(0, n + 1):
            x = i * h1 + a
            y = fyn(x)
            if integ == -1:
                integ = y
            elif i % 2 == 1:
                ko1 += y
            elif i == n:
                integ += y
            else:
                ko2 += y
        ins2 =  (h1 / 3) * (integ + (4 * ko1) + (2 * ko2))
    print('Интеграл вычисленный с заданной точностью =', "{0:<14.9g}".format(ins1))
    y = abs(toch - ins1)
    print('Абсолютная ошибка =', "{0:<10.6g}".format(y))
    y = abs((toch - ins1)/toch)
    print('Относительная ошибка =', "{0:<10.6g}".format(y))
