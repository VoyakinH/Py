# Воякин Алексей Янович ИУ7-14б
# Защита Графика


# Ввод данных
X = float(input("Введите начальное значение: "))
Y = float(input("Введите конечное значение: "))
Sh = float(input("Введите шаг: "))
print()


# Определение максимума и минимума функции
min = X ** 2 - 49
max = min
# Выполнение
Zn = X
while abs(Zn - Y) >= (10 ** (-10)):
    f = Zn ** 2 - 49
    Zn += Sh
    if max < f:
        max = f
    if min > f:
        min = f
print('-' * (len(str(X + Sh)) + 75))
otgl = -1
otgl = ( -7 - min) / (max - min) * 70
if X > Y and min < 0 and max > 0:
    print(' ' * (len(str(X)) - 2), 'X'," " * (len(str(Sh)) - 3), "|", " " *  (int(otgl) - 2), "|")
if X < Y and min < 0 and max > 0:
    print(' ' * (len(str(Y)) - 1), 'X'," " * (len(str(Sh)) - 3), "|", " " *  (int(otgl) - 2), "|")
if X > Y and (min > 0 or max < 0):
    print(' ' * (len(str(X)) - 2), 'X'," " * (len(str(Sh)) - 3), "|")
if X < Y and (min > 0 or max < 0):
    print(' ' * (len(str(Y)) - 1), 'X'," " * (len(str(Sh)) - 3), "|")
Zn = X
while abs(Zn - Y) >= (10 ** (-10)):
    f = Zn ** 2 -49
    Zn += Sh
    ot = (f - min) / (max - min) * 70
    if otgl != -1:
        if X > Y:
            print(Zn, " " * (len(str(X)) - len(str(Zn + Sh)) + 1 + 3), "|")
