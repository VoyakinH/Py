# Начертить график функции f1 = z * lg z + 0.125  и f2 = 3z-e**z
# с помощью while
# Трунцев Георгий ИУ7-14б

# Ввести шаг, начальное и конечное значение х 



import math as m

Xn,Xk = map(float, input("Введите начальное и конечное значение X: ").split(","))
h = float(input("Введите шаг: "))
x = Xn
print("X   |    Y   |")
while x <= Xk :
    y = x * 3 - m.exp(x)
    print("%.1f" %(x),"|","%.4f" %(y),"|")
    x = x + h



Xn,Xk = map(float, input("Введите начальное и конечное значение X: ").split(","))
h = float(input("Введите шаг: "))
x = Xn
print("X   |    Y   |")
while x <= Xk :
    if x > 0:
        y = x * m.log10(x) + 0.125
        if x == Xn :
            Ymax = y
            Ymin = x
        if y > Ymax :
            Ymax = y
        if y < Ymin :
            Ymin = y
        print("%.1f" %(x),"|","%.4f" %(y),"|")
    x = x + h
    

print("y = x * log10(x) + 0.125")

x = Xn
print(" ",round(Ymin,2)," "* 68 , round(Ymax,2))
print("x","-"*69)
while x <= Xk :
    if x > 0:
        y = x * m.log10(x) + 0.125
        ras = (y - Ymin ) / (Ymax - Ymin) * 70
        ras = round(ras)
        print(round(x,2)," " * (ras - 1),"*")
    x = x + h
    
