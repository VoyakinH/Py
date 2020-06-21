# Защита уточнения корней
from math import sin

def f(x):
    return sin(x)


def sec(a, b, eps, m):
    if f(a) * f(b) > 0 or f(a) == 0:
        return
    N = 0
    x0 = b
    x1 = b - (b - a) / 1000
    while (abs(x1 - x0) > eps):
        if N > m:
            print("Превышение кол-ва итераций на отрезке ", format(x0, '.4f'), '-', format(x1, '.4f'))
            return
        tmp = x1
        x1 = x1 - (x1 - x0) * f(x1) / (f(x1) - f(x0))
        if not a <= x1 <= b:
            x0 = a
            x1 = a + (b - a) / 1000
            while (abs(x1 - x0) > eps):
                tmp = x1
                x1 = x1 - (x1 - x0) * f(x1) / (f(x1) - f(x0))
                x0 = tmp
                N += 1
                if not a <= x1 <= b:
                    print("На отрезке ", format(x0, '.4f'), '-', format(x1, '.4f'), " секущая не сошлась")
                    return
            print("Корень: ", format(x1, '.4f'), ' ', "Значение корня: ", format(f(x1), '.4f'))
            return
        x0 = tmp
        N += 1
    print("Корень: ", format(x1, '.4f'), ' ', "Значение корня: ", format(f(x1), '.4f'))
    return


a = float(input('Введите начало отрезка: '))
b = float(input('Введите конец отрезка: '))
step = float(input('Введите шаг: '))
eps = float(input('Введите точность: '))
m = int(input('Введите максимальное число итераций: '))

h = a
while h < b:
    if h + step > b:
        step = b - h
    sec(h, h + step, eps, m)
    h += step
