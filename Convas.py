# Выполнил Воякин Алексей Янович ИУ7-24Б
# Лабораторная работа №4


from tkinter import *
from math import *
from tkinter import messagebox as mb

# Объявление переменных и констант
count_circles = 0
circles = list()
count_points = 0
points = list()
canH = 600
canW = 600
min_x, min_y, max_x, max_y, coef = 0, 0, 0, 0, 0

# Выполнение программы.
def resolve():
    # Получение координат, радиусов и занесение их в массив.
    ent_ans_1.delete(0, END)
    ent_ans_2.delete(0, END)
    try:
        arr_toch = [float(i) for i in ent_toch.get().split()]
        arr_circ = [float(i) for i in ent_circ.get().split()]
    except:
        mb.showerror("Неверный ввод", "Некорректный ввод в одном из полей.")
        return

    if len(arr_toch) % 2 != 0:
        mb.showerror("Неверный ввод в первом поле!", "У точки должно быть две координаты.")
        return

    if len(arr_circ) % 3 != 0:
        mb.showerror("Неверный ввод во втором поле!",
                     "У окружности должно быть две координаты и радиус (3 параметра через пробел).")
        return

    if len(arr_toch) == 0:
        mb.showerror("Неверный ввод в первом поле!", "Первое поле не может быть пустым.")
        return

    if len(arr_toch) < 4:
        mb.showerror("Неверный ввод в первом поле!", "Для построения отрезка точек должно быть минимум две.")
        return

    if len(arr_circ) < 3:
        mb.showerror("Неверный ввод во втором поле!", "Второе поле не должно быть пустым.")
        return

    i = 0
    set_of_toch = []
    while i < len(arr_toch):
        set_of_toch.append((arr_toch[i], arr_toch[i + 1]))
        i += 2

    i = 0
    set_of_circ = []
    while i < len(arr_circ):
        set_of_circ.append((arr_circ[i], arr_circ[i + 1], arr_circ[i + 2]))
        i += 3

    # Создание Конвас окна.
    window = Tk()
    window.title("Графическое изображение результатов.")
    window.config(bg = "#eeeeee")
    window.geometry("610x650")

    c = Canvas(window, width = canW, height = canH, bg = 'white')
    min_x = set_of_toch[0][0]
    min_y = set_of_toch[0][1]
    max_x = set_of_toch[0][0]
    max_y = set_of_toch[0][1]

    for i in range(1, len(set_of_toch)):
       x_t = set_of_toch[i][0]
       y_t = set_of_toch[i][1]
       if x_t > max_x:
           max_x = x_t
       if x_t < min_x:
           min_x = x_t
       if y_t > max_y:
           max_y = y_t
       if y_t < min_y:
           min_y = y_t

    for i in range(0, len(set_of_circ)):
       x_t = set_of_circ[i][0]
       y_t = set_of_circ[i][1]
       r_t = set_of_circ[i][2]
       if x_t + r_t> max_x:
           max_x = x_t + r_t
       if x_t - r_t < min_x:
           min_x = x_t - r_t
       if y_t + r_t > max_y:
           max_y = y_t + r_t
       if y_t - r_t < min_y:
           min_y = y_t - r_t

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

    for i in range(0, len(set_of_circ)):
        x_t = 10 + (set_of_circ[i][0] - set_of_circ[i][2] - min_x) * coef
        y_t = canH - (10 + (set_of_circ[i][1] - set_of_circ[i][2] - min_y) * coef)
        x_t_2 = 10 + (set_of_circ[i][0] + set_of_circ[i][2] - min_x) * coef
        y_t_2 = canH - (10 + (set_of_circ[i][1] + set_of_circ[i][2] - min_y) * coef)
        c.create_oval(x_t, y_t, x_t_2, y_t_2, width = 4, outline = 'blue')

    for i in range(0, len(set_of_toch)):
        x_t = 10 + (set_of_toch[i][0] - min_x) * coef
        y_t = canH - (10 + (set_of_toch[i][1] - min_y) * coef)
        c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'black')
    c.create_line(0, canH - (10 + (0 - min_y) * coef), 600, canH - (10 + (0 - min_y) * coef), fill='green', width=3)
    c.create_line(10 + (0 - min_x) * coef, 0, 10 + (0 - min_x) * coef, 600, fill='green', width=3)
    c.place(x = 0, y = 50)

    chosen = [-1, -1]
    max_in = -1
    for i in range(0, len(set_of_toch) - 1):
        for j in range(i + 1, len(set_of_toch)):
            if set_of_toch[i][0] == set_of_toch[j][0] and set_of_toch[i][1] == set_of_toch[j][1]:
                continue
            x1 = set_of_toch[i][0]
            y1 = set_of_toch[i][1]
            x2 = set_of_toch[j][0]
            y2 = set_of_toch[j][1]

            cur_in = 0
            for k in range(0, len(set_of_circ)):
                xc = set_of_circ[k][0]
                yc = set_of_circ[k][1]
                
                if fabs(x2 - x1) < 1e-7:
                    r = fabs(x2 - xc)
                elif fabs(y2 - y1) < 1e-7:
                    r = fabs(y2 - yc)
                else:
                    y = (xc - x1) * (y2 - y1) / (x2 - x1) + y1
                    x = (yc - y1) * (x2 - x1) / (y2 - y1) + x1
                    r = sqrt((x - xc) * (x - xc) + (y - yc) * (y - yc)) / 2

                if r <= set_of_circ[k][2]:
                    cur_in += 1
               

            if cur_in > max_in:
                chosen = [i, j]
                max_in = cur_in
                
    if max(chosen) == -1:
        mb.showerror("Невозможность создания прямой.", "Через данные точки невозможно провести прямую!")
    else:
        ent_ans_1.insert(0, set_of_toch[int(chosen[0])])
        ent_ans_2.insert(0, set_of_toch[int(chosen[1])])
        for i in range(2):
            x_t = 10 + (set_of_toch[chosen[i]][0] - min_x) * coef
            y_t = canH - (10 + (set_of_toch[chosen[i]][1] - min_y) * coef)
            c.create_oval(x_t, y_t, x_t, y_t, outline = "red", width = 8)

        fromX1 = 10 + (set_of_toch[chosen[0]][0] - min_x) * coef
        fromY1 = 10 + (set_of_toch[chosen[0]][1] - min_y) * coef
        toX1 = 10 + (set_of_toch[chosen[1]][0] - min_x) * coef
        toY1 = 10 + (set_of_toch[chosen[1]][1] - min_y) * coef
        if toY1 != fromY1:
            fromX = (0 - fromY1) / (toY1 - fromY1) * (toX1 - fromX1) + fromX1
            toX = (canH - fromY1) / (toY1 - fromY1) * (toX1 - fromX1) + fromX1
            fromY = canH
            toY = 0
        else:
            fromX = 0
            toX = canW
            fromY = canH - fromY1
            toY = canH - fromY1
        
        c.create_line(fromX, fromY, toX, toY)
    window.mainloop()

    

# Создание окна.
root = Tk()
root.title('Л.Р №4')
root.geometry('680x280')
root.configure(background='#FAEBD7')

# Задание основных параметров.
title_tochki = Label(root, text='Введите координаты точек через пробел', background='#FAEBD7', font=('times', 18))
ent_toch = Entry(root, width=70, font = '18')
title_circ = Label(root, text='Введите координаты и радиусы окружностей через пробел', background='#FAEBD7', font=('times', 18))
ent_circ = Entry(root, width=70, font = '18')
resolve_button = Button(root,  text='Вычислить', font=('times', 18), command=resolve)
title_ans_1 = Label(root, text='Координаты первой полученной точки', background='#FAEBD7', font=('times', 16))
ent_ans_1 = Entry(root, width=34)
title_ans_2 = Label(root, text='Координаты второй полученной точки', background='#FAEBD7', font=('times', 16))
ent_ans_2 = Entry(root, width=34)


# Размещение на экране;
title_tochki.place(x=180, y=10)
ent_toch.place(x=20, y=40)
title_circ.place(x=120, y=80)
ent_circ.place(x=20, y=110)
resolve_button.place(x=285, y=150)
title_ans_1.place(x=45, y=200)
ent_ans_1.place(x=20, y=230)
title_ans_2.place(x=370, y=200)
ent_ans_2.place(x=345, y=230)

root.mainloop()
