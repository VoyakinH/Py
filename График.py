# Воякин Алексей Янович ИУ7-14Б
# Вывести таблицу значений функций и построить график


# Ввод данных
X1 = int(input("Введите начальное значение : "))
X2 = int(input("Введите конечное значение : "))
Sh = float(input("Введите шаг: "))
print()


# Заносим начальные значения в min и max функций
min1 = X1 ** X1 + 2 * X1 - 6
max1 = min1
min2 = X1 ** 3 - X1 - 1
max2 = min2
min3 = (abs(min1 * min2)) ** (1 / 2)
max3 = min3


# Выполнение программы
if Sh < 0:
    k = 3
    ke = -1
else:
    k = 2
    ke = 1
if Sh < 1:
    print('-' * (len(str(X2)) + len(str(Sh)) + 47))
    print(' ' * (len(str(X2)) - 1), 'X', ' ' * (len(str(Sh)) - k), '|', ' ' * 4, "G1", ' ' * 4, '|',
          ' ' * 4, "G2", ' ' * 4, '|', ' ' * 4, "G3", ' ' * 4, '|')
    step = 1 / Sh
    step = int(step)
    if X2 < X1:
        H = -1
    else:
        H = 1
    for i in range(X1, X2, H):
        for j in range(0, step, H):
            x = round((ke * j * Sh + i), len(str(Sh)) - k)
            g1 = abs(pow(x, x)) + 2 * x - 6
            if g1 > max1:
                max1 = g1
            if g1 < min1:
                min1 = g1
            g2 = x ** 3 - x - 1
            if g2 > max2:
                max2 = g2
            if g2 < min2:
                min2 = g2
            g3 = (abs(g1 * g2)) ** (1 / 2)
            if g3 > max3:
                max3 = g3
            if g3 < min3:
                min3 = g3
            print(x, ' ' * (len(str(X2 + Sh)) - len(str(x))), '|',
                  '{:.5g}'.format(g1), ' ' * (11 - len(str('{:.5g}'.format(g1)))), '|',
                  '{:.5g}'.format(g2), ' ' * (11 - len(str('{:.5g}'.format(g2)))), '|',
                  '{:.5g}'.format(g3), ' ' * (11 - len(str('{:.5g}'.format(g3)))), '|')
            if i == (X2 - (ke * 1)) and j == (step - (ke * 1)):
                x = round((ke * j * Sh + i), len(str(Sh)) - k)
                x += Sh
                g1 = abs(x ** x) + 2 * x - 6
                if g1 > max1:
                    max1 = g1
                if g1 < min1:
                    min1 = g1
                g2 = x ** 3 - x - 1
                if g2 > max2:
                    max2 = g2
                if g2 < min2:
                    min2 = g2
                g3 = (abs(g1 * g2)) ** (1 / 2)
                if g3 > max3:
                    max3 = g3
                if g3 < min3:
                    min3 = g3
                print(x, ' ' * (len(str(X2 + Sh)) - len(str(x))), '|',
                      '{:.5g}'.format(g1), ' ' * (11 - len(str('{:.5g}'.format(g1)))), '|',
                      '{:.5g}'.format(g2), ' ' * (11 - len(str('{:.5g}'.format(g2)))), '|',
                      '{:.5g}'.format(g3), ' ' * (11 - len(str('{:.5g}'.format(g3)))), '|')
    print('-' * (len(str(X2)) + len(str(Sh)) + 47))
    print('-' * (len(str(X2)) + 75 + (len(str(Sh)))))
    print(' ' * (len(str(X2)) - 1), 'X', ' ' * (len(str(Sh)) - k), '|')
    for i in range(X1, X2, H):
        for j in range(0, step, H):
            x = round((ke * j * Sh + i), len(str(Sh)) - k)
            g1 = abs(pow(x, x)) + 2 * x - 6
            ot = (g1 - min1)/(max1 - min1)*70
            print(x, ' ' * (len(str(X2 + Sh)) - len(str(x))), '|', ' ' * (int(ot)), '*')
            if i == (X2 - (ke * 1)) and j == (step - (ke * 1)):
                x = round((ke * j * Sh + i), len(str(Sh)) - k)
                x += Sh
                g1 = abs(x ** x) + 2 * x - 6
                ot = (g1 - min1) / (max1 - min1) * 70
                print(x, ' ' * (len(str(X2 + Sh)) - len(str(x))), '|', ' ' * (int(ot)), '*')
elif Sh >= 1:
    print('-' * (len(str(X2)) + len(str(Sh)) + 45))
    if len(str(X2)) > 1:
        print(' ' * (len(str(X2)) - 2), 'X', ' ' * (len(str(X2)) - 2), '|', ' ' * 4, "G1", ' ' * 4, '|',
              ' ' * 4, "G2", ' ' * 4, '|', ' ' * 4, "G3", ' ' * 4, '|')
    else:
        print(' ' * (len(str(X2)) - 2), 'X', '|', ' ' * 4, "G1", ' ' * 4, '|',
              ' ' * 4, "G2", ' ' * 4, '|', ' ' * 4, "G3", ' ' * 4, '|')
    Sh = int(Sh)
    x = X1
    for x in range(X1, X2 + 1, Sh):
        g1 = abs(pow(x, x)) + 2 * x - 6
        if g1 > max1:
            max1 = g1
        if g1 < min1:
            min1 = g1
        g2 = x ** 3 - x - 1
        if g2 > max2:
            max2 = g2
        if g2 < min2:
            min2 = g2
        g3 = (abs(g1 * g2)) ** (1 / 2)
        if g3 > max3:
            max3 = g3
        if g3 < min3:
            min3 = g3
        print(x, ' ' * ((len(str(X2)) - 2) + (len(str(X2)) - 2) + 2 - len(str(x))), '|',
              '{:.5g}'.format(g1), ' ' * (11 - len(str('{:.5g}'.format(g1)))), '|',
              '{:.5g}'.format(g2), ' ' * (11 - len(str('{:.5g}'.format(g2)))), '|',
              '{:.5g}'.format(g3), ' ' * (11 - len(str('{:.5g}'.format(g3)))), '|')
    print('-' * (len(str(X2)) + len(str(Sh)) + 47))
    print('-' * (len(str(X2)) + 75 + (len(str(Sh)))))
    if len(str(X2)) > 1:
        print(' ' * (len(str(X2)) - 2), 'X', ' ' * (len(str(X2)) - 2), '|')
    else:
        print(' ' * (len(str(X2)) - 2), 'X', '|')
    for x in range(X1, X2 + 1, Sh):
        g1 = abs(pow(x, x)) + 2 * x - 6
        ot = (g1 - min1)/(max1 - min1)*70
        print(x, ' ' * (len(str(X2 + Sh)) - len(str(x))), '|', ' ' * (int(ot)), '*')
