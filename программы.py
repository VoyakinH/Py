#Ввести 3 точки и проверить, является ли треугольник прямоугольным
#Воробьев Семен Дмитриевич ИУ7-14Б

#ВВод данных

from math import sqrt

Ax = int(input('Введите координату X точки A: '))
Ay = int(input('Введите координату Y точки A: '))
Bx = int(input('Введите координату X точки B: '))
By = int(input('Введите координату Y точки B: '))
Cx = int(input('Введите координату X точки C: '))
Cy = int(input('Введите координату Y точки C: '))

degAB = acos((BC ** 2 + (AC ** 2) - (AB ** 2)) / (2 * BC * AC))
degBC = acos((AB ** 2 + (AC ** 2) - (BC ** 2)) / (2 * AB * AC))
degAC = acos((AB ** 2 + (BC ** 2) - (AC ** 2)) / (2 * AB * BC))
degAB = round(degAB, 7)             
degBC = round(degBC, 7)
degAC = round(degAC, 7)
p = round((pi / 2), 7)
if degAB == p or degAC == p or degBC == p:
    print("Треугольник ABC является прямоугольным")
else:
    print('Треугольник не является прямоугольным')
