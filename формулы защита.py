# Воякин Алексей Янович ИУ7-14б
# Защита Графика


# Ввод данных
X = float(input("Введите начальное значение: "))
Y = float(input("Введите конечное значение: "))
Sh = float(input("Введите шаг: "))
print()


# Определение максимума и минимума функции
min1 = X ** 2 - 49
max1 = min1
# Выполнение
Zn = X
if X > Y:
    while Zn >= Y:
        f = Zn ** 2 - 49
        Zn += Sh
        if max1 < f:
            max1 = f
        if min1 > f:
            min1 = f
else:
    while Zn <= Y:
        f = Zn ** 2 - 49
        Zn += Sh
        if max1 < f:
            max1 = f
        if min1 > f:
            min1 = f
print('-' * (len(str(X + Sh)) + 73))
ot1 = (0 - min1) / (max1 - min1) * 70
ot1 = int(ot1)
Zn = X
if (X > Y) and (min1 < 0) and (max1 > 0):
    print(' ' * (len(str(X)) - 2), 'X', " " * (len(str(Sh)) - 2), "|", " " * (int(ot1)), "|", sep='')
    while Zn >= Y:
        f = Zn ** 2 - 49
        ot2 = (f - min1) / (max1 - min1) * 70
        ot2 = int(ot2)
        if ot2 > ot1:
            print(Zn, ' ' * (len(str(X)) + len(str(Sh)) - 3 - len(str(Zn))), '|', " " * (int(ot1)),
                  "|", ' ' * (int(ot2) - int(ot1) - 2), '*', sep='')
        elif ot1 > ot2:
            print(Zn, ' ' * (len(str(X)) + len(str(Sh)) - 3 - len(str(Zn))), '|', " " * (int(ot2)),
                  "*", " " * (int(ot1) - int(ot2) - 1), '|', sep='')
        elif ot1 == ot2:
            print(Zn, ' ' * (len(str(X)) + len(str(Sh)) - 3 - len(str(Zn))), '|',
                  ' ' * (int(ot1)), '*', sep='')
        Zn += Sh
        Zn = round(Zn, len(str(Sh)) - 3)
if (X < Y) and (min1 < 0) and (max1 > 0):
    print(' ' * (len(str(Y)) - 1), 'X', " " * (len(str(Sh)) - 2), '|', " " * (int(ot1)), "|", sep='')
    while Zn <= Y:
        f = Zn ** 2 - 49
        ot2 = (f - min1) / (max1 - min1) * 70
        ot2 = int(ot2)
        if ot2 > ot1:
            print(Zn, ' ' * (len(str(X)) + len(str(Sh)) - 3 - len(str(Zn))), '|', " " * (int(ot1)),
                  "|", ' ' * (int(ot2) - int(ot1) - 2), '*', sep='')
        elif ot1 > ot2:
            print(Zn, ' ' * (len(str(X)) + len(str(Sh)) - 3 - len(str(Zn))), '|', " " * (int(ot2)),
                  "*", " " * (int(ot1) - int(ot2) - 1), '|', sep='')
        elif ot1 == ot2:
            print(Zn, ' ' * (len(str(X)) + len(str(Sh)) - 3 - len(str(Zn))), '|',
                  ' ' * (int(ot1)), '*', sep='')
        Zn += Sh
        Zn = round(Zn, len(str(Sh)) - 2)
if X > Y and ((min1 <= 0 and max1 <= 0) or (min1 >= 0 and max1 >= 0)):
    print(' ' * (len(str(X)) - 2), 'X', " " * (len(str(Sh)) - 2), "|", sep='')
    while Zn >= Y:
        f = Zn ** 2 - 49
        ot2 = (f - min1) / (max1 - min1) * 70
        ot2 = int(ot2)
        print(Zn, ' ' * (len(str(X)) + len(str(Sh)) - 3 - len(str(Zn))), '|',
              ' ' * (int(ot2)), '*', sep='')
        Zn += Sh
        Zn = round(Zn, len(str(Sh)) - 3)
if X < Y and ((min1 <= 0 and max1 <= 0) or (min1 >= 0 and max1 >= 0)):
    print(' ' * (len(str(Y)) - 2), 'X', " " * (len(str(Sh)) - 1), "|", sep='')
    while Zn <= Y:
        f = Zn ** 2 - 49
        ot2 = (f - min1) / (max1 - min1) * 70
        ot2 = int(ot2)
        print(Zn, ' ' * (len(str(X)) + len(str(Sh)) - 3 - len(str(Zn))), '|',
              ' ' * (int(ot2)), '*', sep='')
        Zn += Sh
        Zn = round(Zn, len(str(Sh)) - 2)
print('-' * (len(str(X + Sh)) + 73))
