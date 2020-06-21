# Воякин Алексей Янович ИУ7-14Б
# На плоскости заданы координаты трех точек... (Лабораторная работа №3)

from math import sqrt, acos, pi

# Ввод данных
Ax = int(input('Введите координату x точки A: '))
Ay = int(input('Введите координату y точки A: '))
Bx = int(input('Введите координату x точки B: '))
By = int(input('Введите координату y точки B: '))
Cx = int(input('Введите координату x точки C: '))
Cy = int(input('Введите координату y точки C: '))
print()


# Нахождение длин сторон треугольника
AB = sqrt((Ax - Bx) ** 2 + ((Ay - By) ** 2))
BC = sqrt((Bx - Cx) ** 2 + ((By - Cy) ** 2))
AC = sqrt((Ax - Cx) ** 2 + ((Ay - Cy) ** 2))


# Проверка существования треугольника
cont = 0
if (AB + BC > AC) and (AB + AC > BC) and (BC + AC > AB):                             # Сумма двух сторон больше третьей
    cont = 1
else:
    print("Существование треугольника невозможно")


# Вывод длин сторон треугольника
if cont == 1:
    print("Длина AB =", '{:.5g}'.format(AB))
    print("Длина BC =", '{:.5g}'.format(BC))
    print("Длина AC =", '{:.5g}'.format(AC))
    print()


# Нахождение углов треугольника и нахождение наименьшего из них
    degAB = acos((BC ** 2 + (AC ** 2) - (AB ** 2)) / (2 * BC * AC))                  # Представление теоремы косинусов
    degBC = acos((AB ** 2 + (AC ** 2) - (BC ** 2)) / (2 * AB * AC))
    degAC = acos((AB ** 2 + (BC ** 2) - (AC ** 2)) / (2 * AB * BC))
    deg = degAB
    ind = 1
    if degBC < deg:                                                                  # Нахождение наименьшего угла
        deg = degBC
        ind = 2
    if degAC < deg:
        deg = degAC
        ind = 3
    if AB == BC and BC == AC and AC == AB:
        print("Треугольник ABC равносторонний")
    elif (AB == BC) or (AB == AC) or (BC == AC):
        print("Треугольник ABC равнобедренный")
        if ind == 1 and AB == AC:
            print("Наименьшие углы = ABC; BCA")
        elif ind == 1 and AB == BC:
            print("Наименьшие углы = BAC; BCA")
        elif ind == 2 and BC == AC:
            print("Наименьшие углы = BAC; ABC")
    else:
        if ind == 1:
            print("Наименьший угол = BCA")
        elif ind == 2:
            print("Наименьший угол = BAC")
        else:
            print("Наименьший угол = ABC")
    print()


# Нахождение высоты проведенной из наименьшего угла
    pol = (AB + BC + AC) / 2                                                     # Нахождение полупериметра треугольника
    H = 2 * sqrt(pol * (pol - AB) * (pol - BC) * (pol - AC))                     # Формула высоты через полупериметр
    if ind == 1:
        H = H / AB
    elif ind == 2:
        H = H / BC
    else:
        H = H / AC
    print("Высота проведённая из наименьшего угла треугольника ABC =", '{:.5g}'.format(H))
    print()


# Ввод координат четвёртой точки
    Dx = int(input('Введите координату x точки D: '))
    Dy = int(input('Введите координату y точки D: '))
    print()


# Проверка принадлежности точки треугольнику
    Pro1 = (Ax - Dx) * (By - Ay) - ((Bx - Ax) * (Ay - Dy))                       # Векторное произведение
    Pro2 = (Bx - Dx) * (Cy - By) - ((Cx - Bx) * (By - Dy))
    Pro3 = (Cx - Dx) * (Ay - Cy) - ((Ax - Cx) * (Cy - Dy))
    if (Pro1 == 0 and ans(Pro2) > 10 ** (-10) and abs(Pro3) > 10 ** (-10)) or (Pro1 == 0 and abs(Pro2) < 10 ** (-10) and abs(Pro3) < 10 ** (-10)) or \
            (Pro2 == 0 and abs(Pro1) > 10 ** (-10) and abs(Pro3) > 10 ** (-10)) or (Pro2 == 0 and abs(Pro1) < 10 ** (-10) and abs(Pro3) < 10 ** (-10)) or \
            (Pro3 == 0 and abs(Pro1) > 10 ** (-10) and abs(Pro2) > 10 ** (-10)) or (Pro3 == 0 and abs(Pro1) < 10 ** (-10) and abs(Pro2) < 10 ** (-10)) or \
            (Pro1 == 0 and Pro2 == 0 and abs(Pro3) > 10 ** (-10)) or (Pro1 == 0 and Pro2 == 0 and abs(Pro3) < 10 ** (-10)) or \
            (Pro1 == 0 and Pro3 == 0 and abs(Pro2) > 10 ** (-10)) or (Pro1 == 0 and Pro3 == 0 and abs(Pro2) < 10 ** (-10)) or \
            (Pro2 == 0 and Pro3 == 0 and abs(Pro1) > 10 ** (-10)) or (Pro2 == 0 and Pro3 == 0 and abs(Pro1) < 10 ** (-10)):
        print("Точка D лежит на одной из сторон треугольника ABC")
    elif (abs(Pro1) > 10 ** (-10) and abs(Pro2) > 10 ** (-10) and abs(Pro3) > 10 ** (-10)) or\
        (abs(Pro1) < 10 ** (-10) and abs(Pro2) < 10 ** (-10) and abs(Pro3) < 10 ** (-10)):
        print("Точка D лежит внутри треугольника ABC")
    else:
        print("Точка D лежит вне треугольника ABC")


# Нахождение уранений прямых и нахождение расстояния от точки D до ближайшей стороны ABC или ее продолжения
    if (abs(Pro1) > 10 ** (-10) and abs(Pro2) > 10 ** (-10) and abs(Pro3) > 10 ** (-10)) or\
       (abs(Pro1) < 10 ** (-10) and abs(Pro2) < 10 ** (-10) and abs(Pro3) < 10 ** (-10)):
        if (Bx - Ax) != 0:
            k1 = (By - Ay) / (Bx - Ax)
            b1 = Ay - (k1 * Ax)
            DH1 = (abs((-k1) * Dx + Dy - b1)) / (sqrt(k1 ** 2 + 1))
        else:
            DH1 = abs(Ax - Dx)
        if (Cx - Bx) != 0:
            k2 = (Cy - By) / (Cx - Bx)
            b2 = By - (k2 * Bx)
            DH2 = (abs((-k2) * Dx + Dy - b2)) / (sqrt(k2 ** 2 + 1))
        else:
            DH2 = abs(Cx - Dx)
        if (Ax - Cx) != 0:
            k3 = (Ay - Cy) / (Ax - Cx)
            b3 = Cy - (k3 * Cx)
            DH3 = (abs((-k3) * Dx + Dy - b3)) / (sqrt(k3 ** 2 + 1))
        else:
            DH3 = abs(Ax - Dx)
        DHm = DH1
        if DH2 < DHm:
            DHm = DH2
        if DH3 < DHm:
            DHm = DH3
        print("Расстояние от точки D до ближайшей стороны треугольника ABC =", '{:.5g}'.format(DHm))
        print()


# Проверка тупоугольности треугольника
    degAB = round(degAB, 7)                                                   # Округление углов в радианах
    degBC = round(degBC, 7)
    degAC = round(degAC, 7)
    p = round((pi / 2), 7)                                                    # Округление Pi  в радианах
    if degAB > p or degAC > p or degBC > p:
        print("Треугольник ABC является тупоугольным")
    elif degAB == p or degAC == p or degBC == p:
        print("Треугольник ABC является прямоугольным")
    else:
        print("Треугольник ABC является остроугольным")
