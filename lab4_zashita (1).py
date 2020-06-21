from tkinter import *
from math import *
# (x2-x1)(x3-x2) + (y2-y1)(y3-y2) = (x3-x2)(x4-x3) == (y3-y2)(y4-y3) = (x4-x3)(x1-x4) + (y4-y3)(y1-y4) =
#(x1-x4)(x2-x1) + (y1-y4)(y2-y1) = 0


count_points = 0
points = []
canH = 300
canW = 400
min_x, min_y, max_x, max_y, coef = 0, 0, 0, 0, 0

def pryam(x1, y1, x2, y2, x3, y3, x4, y4):
    
    if (x2-x1)*(x3-x2) + (y2-y1)*(y3-y2) == 0 and (x3-x2)*(x4-x3) + (y3-y2)*(y4-y3) == 0 and  (x4-x3)*(x1-x4) + (y4-y3)*(y1-y4)  == 0 and (x1-x4)*(x2-x1) + (y1-y4)*(y2-y1) == 0:
        answ = 1
    else:
        answ = 0
    return answ

def dl(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1 - y2)**2)

def SQR(x1, y1, x2, y2, x3, y3, x4, y4):
      a =dl(x1,y1,x2,y2)
      b =dl(x2,y2,x3,y3)
      c =dl(x3,y3,x4,y4)
      d =dl(x4,y4,x1,y1)
      if a == b == c == d:
          return a*a
      if a != b:
          return a*b
      if a != c:
          return a*c
      if a != d:
          return a*d
          
def solve():
    max_s = 0
    max_i = 0
    max_j = 0
    max_k = 0
    max_t = 0
    for i in range(count):
        for j in range(count):
            for k in range(count):
                for t in range(count):
                    if i != j != k != t:
                        x1 = points[i][0]
                        y1 = points[i][1]
                        x2 = points[j][0]
                        y2 = points[j][1]
                        x3 = points[k][0]
                        y3 = points[k][1]
                        x4 = points[t][0]
                        y4 = points[t][1]
                        if pryam(x1, y1, x2, y2, x3, y3, x4, y4) == 1:
                            if SQR(x1, y1, x2, y2, x3, y3, x4, y4) > max_s:
                                max_s = SQR(x1, y1, x2, y2, x3, y3, x4, y4)
                                max_i = i
                                max_j = j
                                max_k = k
                                max_t = t

    chosen = [max_i, max_j, max_k, max_t]
    i = 0
    j = 1
    k = 2
    t = 3
    x1 = 10 + (points[chosen[i]][0] - min_x) * coef
    y1 = canH - (10 + (points[chosen[i]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    x2 = 10 + (points[chosen[j]][0] - min_x) * coef
    y2 = canH - (10 + (points[chosen[j]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    c.create_line(x1, y1, x2, y2)
    
    x1 = 10 + (points[chosen[i]][0] - min_x) * coef
    y1 = canH - (10 + (points[chosen[i]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    x2 = 10 + (points[chosen[k]][0] - min_x) * coef
    y2 = canH - (10 + (points[chosen[k]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    c.create_line(x1, y1, x2, y2)

    x1 = 10 + (points[chosen[i]][0] - min_x) * coef
    y1 = canH - (10 + (points[chosen[i]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    x2 = 10 + (points[chosen[t]][0] - min_x) * coef
    y2 = canH - (10 + (points[chosen[t]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    c.create_line(x1, y1, x2, y2)


    x1 = 10 + (points[chosen[j]][0] - min_x) * coef
    y1 = canH - (10 + (points[chosen[j]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    x2 = 10 + (points[chosen[i]][0] - min_x) * coef
    y2 = canH - (10 + (points[chosen[i]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    c.create_line(x1, y1, x2, y2)

    x1 = 10 + (points[chosen[j]][0] - min_x) * coef
    y1 = canH - (10 + (points[chosen[j]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    x2 = 10 + (points[chosen[k]][0] - min_x) * coef
    y2 = canH - (10 + (points[chosen[k]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    c.create_line(x1, y1, x2, y2)

    x1 = 10 + (points[chosen[j]][0] - min_x) * coef
    y1 = canH - (10 + (points[chosen[j]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    x2 = 10 + (points[chosen[t]][0] - min_x) * coef
    y2 = canH - (10 + (points[chosen[t]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    c.create_line(x1, y1, x2, y2)

    x1 = 10 + (points[chosen[k]][0] - min_x) * coef
    y1 = canH - (10 + (points[chosen[k]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    x2 = 10 + (points[chosen[i]][0] - min_x) * coef
    y2 = canH - (10 + (points[chosen[i]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    c.create_line(x1, y1, x2, y2)

    x1 = 10 + (points[chosen[k]][0] - min_x) * coef
    y1 = canH - (10 + (points[chosen[k]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    x2 = 10 + (points[chosen[j]][0] - min_x) * coef
    y2 = canH - (10 + (points[chosen[j]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    c.create_line(x1, y1, x2, y2)

    x1 = 10 + (points[chosen[k]][0] - min_x) * coef
    y1 = canH - (10 + (points[chosen[k]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    x2 = 10 + (points[chosen[t]][0] - min_x) * coef
    y2 = canH - (10 + (points[chosen[t]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    c.create_line(x1, y1, x2, y2)

    x1 = 10 + (points[chosen[t]][0] - min_x) * coef
    y1 = canH - (10 + (points[chosen[t]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    x2 = 10 + (points[chosen[i]][0] - min_x) * coef
    y2 = canH - (10 + (points[chosen[i]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    c.create_line(x1, y1, x2, y2)

    x1 = 10 + (points[chosen[t]][0] - min_x) * coef
    y1 = canH - (10 + (points[chosen[t]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    x2 = 10 + (points[chosen[j]][0] - min_x) * coef
    y2 = canH - (10 + (points[chosen[j]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    c.create_line(x1, y1, x2, y2)

    x1 = 10 + (points[chosen[t]][0] - min_x) * coef
    y1 = canH - (10 + (points[chosen[t]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    x2 = 10 + (points[chosen[k]][0] - min_x) * coef
    y2 = canH - (10 + (points[chosen[k]][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'green')
    c.create_line(x1, y1, x2, y2)





    

lines = []
count = int(input("Введите количество точек: "))

for i in range(count):
    print('Введите координаты точки №', i + 1, ': ')
    l = list(map(int, input().split()))
    points.append(l)
print(points)    
window = Tk()
window.title("Геометрия")
window.config(bg = "#eeeeee")
window.geometry("400x400")

c = Canvas(window, width = canW, height = canH, bg = 'white')
btn = Button(window, bg = "#dd0000", text = "Решить!", command = solve)
min_x = points[0][0]
min_y = points[0][1]
max_x = points[0][0]
max_y = points[0][1]

for i in range(1, len(points)):
    x_t = points[i][0]
    y_t = points[i][1]
    if x_t > max_x:
        max_x = x_t
    if x_t < min_x:
        min_x = x_t
    if y_t > max_y:
        max_y = y_t
    if y_t < min_y:
        min_y = y_t
        
if min_x == max_x:
    coef_x = -1
else:
    coef_x = (canW - 20) / (max_x - min_x)
if min_y == max_y:
    coef_y = -1
else:
    coef_y = (canH - 20) / (max_y - min_y)
        
if coef_x > 0 and coef_y > 0:
    coef = min(coef_x, coef_y)


for i in range(len(points)):
    x_t = 10 + (points[i][0] - min_x) * coef
    y_t = canH - (10 + (points[i][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'black')

c.place(x = 0, y = 50)
btn.place(x = 180, y = 20)
window.mainloop()
