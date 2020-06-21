###Сортировки

#Сотрировка выбором
def vibor(a):
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            if a[j] < a[m]:
                m = j
        a[m], a[i] = a[i], a[m]
    return a

#Сортировка вставками
def vstav(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i
        while j > 0 and a[j-1] > x:
            a[j] = a[j-1]
            j -= 1
        a[j] = x
    return a

#Сортировка вставками с барьером
def vstav_bar(a):
    a = [0] + a
    for i in range(2, len(a)):
        a[0] = a[i]
        j = i
        while a[j-1] > a[0]:
            a[j] = a[j-1]
            j -= 1
        a[j] = a[0]
    return a[1:]

#Сортировка вставками с бинарным поиском
def vstav_bin(a):
    for i in range(1, len(a)):
        x = a[i]
        l = 0
        r = i
        while l < r:
            m = (l + r)//2
            if a[m] <= x:
                l = m + 1
            else:
                r = m
        for j in range(i, l, -1):
            a[j] = a[j-1]
        a[l] = x
    return a

#Сортировка Шелла
def shell(a):
    h = len(a)//2
    while h > 0:
        for i in range(h, len(a)):
            x = a[i]
            j = i
            while j > 0 and a[j-h] > x:
                a[j] = a[j-h]
                j -= h
            a[j] = x
        h //= 2
    return a

#Сортировка пузырьком
def bubble(a):
    for i in range(1, len(a)):
        for j in range(len(a) - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

#Сотировка пузырьком с барьером
def bubble_bar(a):
    bar = len(a) - 1
    while bar > 0:
        i = bar
        bar = 0
        for j in range(i):
            if a[j] > a[j+1]:
                bar, a[j], a[j+1] = j, a[j+1], a[j]
    return a

#Сотрировка Шейкер
def shaker(a):
    l = 0
    r = len(a) - 1
    while l < r:
        for j in range(l, r):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        r -= 1
        for j in range(r, l, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
        l += 1
    return a

#Быстрая сортировка
def quicksort(a, first, last):
    if first >= last:
        return 0
    l = first
    r = last
    x = a[(l+r)//2]
    while l < r:
        while l <= last and a[l] <= x:
            l += 1
        while r >= first and a[r] >= x:
            r -= 1
        if l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
    quicksort(a, first, r)
    quicksort(a, l, last)
    return a
"""
from random import *
a = [randint(-10000, 10000) for i in range(2000)]
b = sorted(a)
if vibor(a) == b: print('Ok', end = ' ')
if vstav(a) == b: print('Ok', end = ' ')
if vstav_bar(a) == b: print('Ok', end = ' ')
if vstav_bin(a) == b: print('Ok', end = ' ')
if shell(a) == b: print('Ok', end = ' ')
if bubble(a) == b: print('Ok', end = ' ')
if bubble_bar(a) == b: print('Ok', end = ' ')
if quicksort(a, 0, len(a) - 1) == b: print('Ok', end = ' ')
print()
"""
### Интегралы

#Функции
def f(x):
    return x**3 - 18*x - 83
def g(x):
    return x ** 3 - 17 * x - 83
def F(x):
    return 0.25*x**4 - 9*x**2 - 83*x
def f1(x):
    return 3*x**2 - 18

#Левые прямоугольники
def left(a,b,n):
    h = (b-a)/n
    int = 0
    for i in range(n):
        int += f(a + i*h)
    return int*h

#Правые прямоугольники
def right(a,b,n):
    h = (b-a)/n
    int = 0
    for i in range(1, n + 1):
        int += f(a + i*h)
    return int * h

#Центральные прямоугольники
def middle(a,b,n):
    h = (b-a)/n
    int = 0
    for i in range(n):
        int += f(a + (i + 0.5)*h)
    return int * h

#Трапеции
def trap(a,b,n):
    h = (b-a)/n
    int = (f(a) + f(b))/2
    for i in range(1, n):
        int += f(a + i*h)
    return int * h

#Метод Симпсона (парабол)
def simpson(a,b,n):
    h = (b-a)/n
    int = f(a) + f(b)
    for i in range(1, n, 2):
        int += f(a + i*h) * 4
    for i in range(2, n, 2):
        int += f(a + i*h) * 2
    return int * h/3

#3/8
def three_eigth(a,b,n):
    h = (b-a)/n
    int = f(a) + f(b)
    for i in range(1, n, 3):
        int += (f(a + i*h) + f(a + (i+1)*h)) * 3
    for i in range(3, n, 3):
        int += f(a + i*h) * 2
    return int * (3/8)*h

#Буль
def booooool(a,b,n):
    h = (b-a)/n
    int = (f(a) + f(b))*7
    for i in range(1, n, 4):
        int += (f(a + i*h) + f(a + (i+2)*h))*32 + f(a + (i+1)*h)*12
    for i in range(4, n, 4):
        int += f(a + i*h) * 14
    return int*2/45*h

#Уэбля
def u_e_blya(a,b,n):
    h = (b - a) / n
    int = f(a) + f(b)
    for i in range(1, n, 6):
        int += (f(a+i*h) + f(a+(i+4)*h))*5 + f(a+(i+2)*h)*6 + f(a+(i+1)*h) + f(a+(i+3)*h)
    for i in range(6, n, 6):
        int += f(a + i*h) * 2
    return int*3/10*h
"""
print(F(6) - F(0))
print(left(0, 6, 120))
print(right(0, 6, 120))
print(middle(0, 6, 120))
print(trap(0, 6, 120))
print(simpson(0, 6, 120))
print(three_eigth(0, 6, 120))
print(booooool(0, 6, 120))
print(u_e_blya(0, 6, 120))
"""

### Уточнение корней
"""
Нулевая точка содержится в отрезке [5;6]
"""

#Метод Ньютона (касательных)
def newton(x0, eps):
    x = x0 - f(x0)/f1(x0)
    while abs(x - x0) > eps:
        x0 = x
        x = x0 - f(x0) / f1(x0)
    return x

#Упрощённый метод касательных
def newton_easy(x0, eps):
    proiz = f1(x0)
    x = x0 - f(x0) / proiz
    while abs(x - x0) > eps:
        x0 = x
        x = x0 - f(x0) / proiz
    return x

#Метод секущих
def sek(x0, x1, eps):
    x = x1 - f(x1)*(x0 - x1)/(f(x0) - f(x1))
    if abs(x0-x) < abs(x1 - x): #Выбираем x1 по близости x0 и x1 к x2
        x0, x1 = x1, x0
    while abs(x1 - x) > eps:
        x0, x1 = x1, x
        x = x1 - f(x1)*(x0 - x1)/(f(x0) - f(x1))
    return x

#Метод хорд
def hord(a,b,eps):
    x = a - f(a)*(b-a)/(f(b) - f(a))
    if f(x)>0:      # Если функция выпукла вверх
        b, a = a,b  # b становится подвижной, a стационарной
    while abs(x - a) > eps:
        a = x
        x = a - f(a)*(b-a)/(f(b) - f(a))
    return x

#Комбинированый метод (хорды + касательные)
def combo(a,b,eps):
    if f(b)*f(b-f(b)/f1(b)) < 0: #К b применяется метод Ньютона
        a, b = b, a              #К a применяется метод хорд
    while abs(a-b)>eps:
        a, b = a - f(a)*(b-a)/(f(b) - f(a)), b - f(b)/f1(b)
    return (a + b)/2

#Метод Стеффенсена
def steff(x0, eps):
    x = x0 - f(x0)**2/(f(x0 + f(x0)) - f(x0))
    while abs(x-x0) > eps:
        x0 = x
        x = x0 - f(x0) ** 2 / (f(x0 + f(x0)) - f(x0))
    return x

#Метод простых итераций
def iterations(x0, eps):
    x = g(x0)
    while abs(x0-x) > eps:
        x0 = x
        x = g(x0)
    return x

#Метод половинного деления
def half(a,b,eps):
    if f(a) > 0:        #f(b)>0
        a, b = b ,a     #f(a)<0
    while abs(a - b) > eps:
        m = (a + b) / 2
        if f(m)<0:
            a = m
        else:
            b = m
    return (a+b)/2

print(newton(6, 0.0001))
print(newton_easy(6, 0.0001))
print(hord(5,6, 0.0001))
print(sek(6,7, 0.0001))
print(combo(5,6, 0.0001))
print(steff(6, 0.0001))
print(half(5,6, 0.0001))
print(iterations(6, 0.0001))
