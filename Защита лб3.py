# Воякин Алексей Янович ИУ7-14б
# Защита 3 лабы

from math import sqrt, acos


# Ввод данных
Ax = int(input('Введите координату x точки A: '))
Ay = int(input('Введите координату y точки A: '))
Bx = int(input('Введите координату x точки B: '))
By = int(input('Введите координату y точки B: '))
Cx = int(input('Введите координату x точки C: '))
Cy = int(input('Введите координату y точки C: '))


# Нахождение длин треугольника ABC
AB = sqrt((Ax - Bx) ** 2 + ((Ay - By) ** 2))
BC = sqrt((Bx - Cx) ** 2 + ((By - Cy) ** 2))
AC = sqrt((Ax - Cx) ** 2 + ((Ay - Cy) ** 2))


# Нахождение наибольшего угла треугольника
degAB = acos((BC ** 2 + (AC ** 2) - (AB ** 2)) / (2 * BC * AC))
degBC = acos((AB ** 2 + (AC ** 2) - (BC ** 2)) / (2 * AB * AC))
degAC = acos((AB ** 2 + (BC ** 2) - (AC ** 2)) / (2 * AB * BC))
deg = degAB
ind = 1
if degBC > deg:
    deg = degBC
    ind = 2
if degAC > deg:
    deg = degAC
    ind = 3


# Нахождение медианы проведённой из наибольшего угла
if ind == 1:
    med = sqrt(2 * (BC ** 2) + (2 * (AC ** 2)) - (AB ** 2)) / 2
elif ind == 2:
    med = sqrt(2 * (AB ** 2) + (2 * (AC ** 2)) - (AC ** 2)) / 2
else:
    med = sqrt(2 * (BC ** 2) + (2 * (AB ** 2)) - (AC ** 2)) / 2
print("Медиана равна: ",'{:.5g}'.format(med))
