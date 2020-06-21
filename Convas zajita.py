from tkinter import *
from math import *
from tkinter import messagebox as mb

canH = 600
canW = 600
min_x, min_y, max_x, max_y, coef = 0, 0, 0, 0, 0

def resolve():
    min_x, min_y, max_x, max_y, coef = 0, 0, 0, 0, 0
    ent_ans_1.delete(0, END)
    ent_ans_2.delete(0, END)
    try:
        arr_toch = [float(i) for i in ent_toch.get().split()]
    except:
        mb.showerror("Неверный ввод", "Некорректный ввод.")
        return

    if len(arr_toch) % 2 != 0:
        mb.showerror("Неверный ввод в поле!", "У точки должно быть две координаты.")
        return

    if len(arr_toch) == 0:
        mb.showerror("Неверный ввод!", "Поле не может быть пустым.")
        return

    if len(arr_toch) < 4:
        mb.showerror("Неверный ввод!", "Для построения отрезка, точек должно быть минимум две.")
        return

    i = 0
    set_of_toch = []
    while i < len(arr_toch):
        set_of_toch.append((arr_toch[i], arr_toch[i + 1]))
        i += 2

    window = Tk()
    window.title("Графическое изображение результатов.")
    window.config(bg="#eeeeee")
    window.geometry("610x610")

    c = Canvas(window, width=canW, height=canH, bg='white')
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


    for i in range(0, len(set_of_toch)):
        x_t = 10 + (set_of_toch[i][0] - min_x) * coef
        y_t = canH - (10 + (set_of_toch[i][1] - min_y) * coef)
        c.create_oval(x_t, y_t, x_t, y_t, width=4, outline='black')

    c.create_line(0, canH - (10 + (0 - min_y) * coef), 600, canH - (10 + (0 - min_y) * coef), fill='green', width=3)
    c.create_line(10 + (0 - min_x) * coef, 0, 10 + (0 - min_x) * coef, 600, fill='green', width=3)

    c.place(x=0, y=0)

    chosen = [-1, -1]
    max_angle = -1
    for i in range(0, len(set_of_toch) - 1):
        for j in range(i + 1, len(set_of_toch)):
            if set_of_toch[i][0] == set_of_toch[j][0] and set_of_toch[i][1] == set_of_toch[j][1]:
                continue
            x1 = set_of_toch[i][0]
            y1 = set_of_toch[i][1]
            x2 = set_of_toch[j][0]
            y2 = set_of_toch[j][1]

            cur_angle = 0
            prilej = abs(x2 - x1)
            if (prilej == 0):
                max_angle = cur_angle
                chosen = [i, j]
                break
            protivolej = abs(y2 - y1)
            cur_angle = atan(protivolej / prilej)
            print(cur_angle)


            if cur_angle > max_angle:
                chosen = [i, j]
                max_angle = cur_angle

    if max(chosen) == -1:
        mb.showerror("Невозможность создания прямой.", "Через данные точки невозможно провести прямую!")
    else:
        ent_ans_1.insert(0, set_of_toch[int(chosen[0])])
        ent_ans_2.insert(0, set_of_toch[int(chosen[1])])
        for i in range(2):
            x_t = 10 + (set_of_toch[chosen[i]][0] - min_x) * coef
            y_t = canH - (10 + (set_of_toch[chosen[i]][1] - min_y) * coef)
            c.create_oval(x_t, y_t, x_t, y_t, outline="red", width=8)

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
root.title('Защита 4 лабы')
root.geometry('680x180')
root.configure(background='#FAEBD7')

# Задание основных параметров.
title_tochki = Label(root, text='Введите координаты точек через пробел', background='#FAEBD7', font=('times', 18))
ent_toch = Entry(root, width=70, font='18')
resolve_button = Button(root, text='Вычислить', font=('times', 18), command=resolve)
title_ans_1 = Label(root, text='Координаты первой полученной точки', background='#FAEBD7', font=('times', 16))
ent_ans_1 = Entry(root, width=34)
title_ans_2 = Label(root, text='Координаты второй полученной точки', background='#FAEBD7', font=('times', 16))
ent_ans_2 = Entry(root, width=34)


# Размещение на экране;
title_tochki.place(x=180, y=10)
ent_toch.place(x=20, y=40)
resolve_button.place(x=285, y=80)
title_ans_1.place(x=45, y=110)
ent_ans_1.place(x=20, y=140)
title_ans_2.place(x=370, y=110)
ent_ans_2.place(x=345, y=140)

root.mainloop()