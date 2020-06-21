from tkinter import *
from tkinter import messagebox as mb
from math import sqrt

# Образуют ли точки треугольник
def is_triangle(a, b, c):
    if ((a[0] - b[0]) * (c[1] - b[1]) - (c[0] - b[0]) * (a[1] - b[1])) == 0:
        return 0
    else:
        return 1

# Площадь треугольника
def area_triangle(a, b, c):
    return 0.5*abs((b[0] - a[0])*(c[1] - a[1]) - (c[0] - a[0])*(b[1] - a[1]))

# Длина вектора
def seg_len(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Биссектрисы
def calculate_bis(a, b, c):
    ab = seg_len(a, b)
    ac = seg_len(a, c)
    bc = seg_len(b, c)
    coeff = ab * bc / (ab + ac)
    vec = (c[0] - b[0], c[1] - b[1])
    return b[0] + vec[0] / bc * coeff, b[1] + vec[1] / bc * coeff

# Какая биссектриса рзбивает треугольники так, чтобы разность площадей была минимальна
def area_triangle_bisectrix(a, b, c):
    bis_a = calculate_bis(a, b, c)
    bis_b = calculate_bis(b, c, a)
    bis_c = calculate_bis(c, a, b)
    min_area = 10000
    vertex = [0, 0]
    if abs(area_triangle(c, a, bis_a) - area_triangle(b, a, bis_a)) < min_area:
        min_area = abs(area_triangle(c, a, bis_a) - area_triangle(b, a, bis_a))
        min_bisectrix = bis_a
        vertex = [a[0], a[1]]
    if abs(area_triangle(c, a, bis_c) - area_triangle(b, c, bis_c)) < min_area:
        min_area = abs(area_triangle(c, a, bis_c) - area_triangle(b, c, bis_c))
        min_bisectrix = bis_c
        vertex = [c[0], c[1]]
    if abs(area_triangle(b, a, bis_b) - area_triangle(b, c, bis_b)) < min_area:
        min_area = abs(area_triangle(b, a, bis_b) - area_triangle(b, c, bis_b))
        min_bisectrix = bis_b
        vertex = [b[0], b[1]]
    ans = []
    ans.append(min_area)
    ans.append(min_bisectrix)
    ans.append(vertex)
    return ans

# Рисование
def make_img(a, b, c, vitrex, min_bisectrix, set_of_points):
    root_graf = Tk()
    MAX_WIDTH = 1000
    MAX_HIGHT = 1000
    CENTER_VERTICAL = 500
    CENTER_HORIZONTAL = 500
    SHIFT_LINE = 5
    SHIFT_TEXT_X = 5
    SHIFT_TEXT_Y = 10
    COUNT_STEPS = 20
    STEP_SIZE = MAX_WIDTH / COUNT_STEPS
    # get start ratio
    min_coord = min(a[0], b[0], c[0], a[1], b[1], c[1])
    max_coord = max(a[0], b[0], c[0], a[1], b[1], c[1])
    if abs(min_coord) < 10 and abs(max_coord) < 10:
        RATIO = 10
        k = 0
    elif abs(min_coord) < 25 and abs(max_coord) < 25:
        RATIO = 25
        k = 3
    elif abs(min_coord) < 50 and abs(max_coord) < 50:
        RATIO = 50
        k = 4
    elif abs(min_coord) < 100 and abs(max_coord) < 100:
        RATIO = 100
        k = 4
    elif abs(min_coord) < 200 and abs(max_coord) < 200:
        RATIO = 200
        k = 4
    else:
        RATIO = 500
        k = 4
    RATIO_STEP = RATIO * 2 / COUNT_STEPS
    # draw ox\oy
    canv = Canvas(root_graf, width=MAX_WIDTH, height=MAX_HIGHT, bg="#C1CACA")
    canv.create_line(CENTER_HORIZONTAL, MAX_HIGHT, CENTER_HORIZONTAL, 0, width=2, arrow=LAST)
    canv.create_line(0, CENTER_VERTICAL, MAX_WIDTH, CENTER_VERTICAL, width=2, arrow=LAST)
    canv.create_text(CENTER_HORIZONTAL - SHIFT_TEXT_X, CENTER_VERTICAL + 2 * SHIFT_TEXT_Y,
                     text=str(0), fill="#1D334A", font=("Helvectica", "9"))
    step = -RATIO
    for i in range(1, COUNT_STEPS):
        current_step = i * STEP_SIZE
        step += RATIO_STEP
        if (current_step - MAX_WIDTH / 2) == 0.0:
            continue
        # draw ocX
        canv.create_line(current_step, CENTER_VERTICAL - SHIFT_LINE,
                         current_step, CENTER_VERTICAL + SHIFT_LINE, width=1, fill='#45322E')
        canv.create_text(current_step, CENTER_VERTICAL + 2 * SHIFT_TEXT_X,
                         text=str(int(step)), fill="#1D334A", font=("Helvectica", "9"))
        # draw ocY
        canv.create_line(CENTER_HORIZONTAL - SHIFT_LINE, current_step,
                         CENTER_HORIZONTAL + SHIFT_LINE, current_step, width=1, fill='#45322E')

        canv.create_text(CENTER_HORIZONTAL - 2 * SHIFT_TEXT_Y, current_step,
                         text=str(-int(step)), fill="#1D334A", font=("Helvectica", "9"))

    def plot_line(a_, b_, color="black"):
        canv.create_line(CENTER_HORIZONTAL + a_[0] * STEP_SIZE / RATIO_STEP,
                         CENTER_VERTICAL - a_[1] * STEP_SIZE / RATIO_STEP,
                         CENTER_HORIZONTAL + b_[0] * STEP_SIZE / RATIO_STEP,
                         CENTER_VERTICAL - b_[1] * STEP_SIZE / RATIO_STEP, fill=color, width = 3)
    plot_line(a, b)
    plot_line(b, c)
    plot_line(c, a)
    point = []
    plot_line(vitrex, min_bisectrix, color="#EF3038")
    for i in set_of_points:
        temp_point = canv.create_oval(CENTER_HORIZONTAL -k + (i[0] - 0.1) * STEP_SIZE / RATIO_STEP,
                                CENTER_VERTICAL +k +(-1)*(i[1] - 0.1) * STEP_SIZE / RATIO_STEP,
                                CENTER_HORIZONTAL + k + (i[0] + 0.1) * STEP_SIZE / RATIO_STEP ,
                                CENTER_VERTICAL - k +(-1)*(i[1] + 0.1) * STEP_SIZE / RATIO_STEP, fill='#EFD334')
        point.append(temp_point)


    canv.create_oval(CENTER_HORIZONTAL -k +(min_bisectrix[0] - 0.1) * STEP_SIZE / RATIO_STEP,
                                CENTER_VERTICAL + k +(-1)*(min_bisectrix[1] - 0.1) * STEP_SIZE / RATIO_STEP,
                                CENTER_HORIZONTAL + k +(min_bisectrix[0] + 0.1) * STEP_SIZE / RATIO_STEP,
                                CENTER_VERTICAL -k +(-1)*(min_bisectrix[1] + 0.1) * STEP_SIZE / RATIO_STEP, fill='#4CBB17')

    canv.pack()
    root_graf.mainloop()


# Обработка точек
def resolve():
    try:
        arr = [float(i) for i in set_entry.get().split()]
    except:
        mb.showerror("Неверный ввод", "Введите данные корректно")
        return

    if len(arr) % 2 != 0:
        mb.showerror("Неверный ввод", "Введено недостаточное количество координат")

    i = 0
    set_of_points = []
    while i < len(arr):
        set_of_points.append((arr[i], arr[i + 1]))
        i += 2


    eps = 0.000001
    min_sum = -1
    a_min = 0
    b_min = 0
    c_min = 0
    count_tringle = 0
    for a in set_of_points:
        for b in set_of_points:
            for c in set_of_points:
                if is_triangle(a, b, c):
                    count_tringle += 1


    if count_tringle == 0:
        mb.showerror("Предупреждение", "Введённые координаты не образуют ни одного треугольника")
        return

    min_area = float(10000)
    for a in set_of_points:
        for b in set_of_points:
            for c in set_of_points:
                if is_triangle(a, b, c):
                    m = area_triangle_bisectrix(a, b, c)
                    area = float(m[0])
                    if float(area) < float(min_area):
                        min_area = float(area)
                        min_bisectrix = m[1]
                        vitrex = m[2]
                        a_min = a
                        b_min = b
                        c_min = c
    s = '[' + str(a_min[0]) + ';' + str(a_min[1]) + '], '
    answ_line.insert(0, s)
    s = '[' + str(b_min[0]) + ';' + str(b_min[1]) + '], '
    answ_line.insert(END, s)
    s = '[' + str(c_min[0]) + ',' + str(c_min[1]) + ']'
    answ_line.insert(END, s)


    make_img(a_min, b_min, c_min, vitrex, min_bisectrix, set_of_points)

# Очистка поля при изменении
def field_clear():  # очистка поля вывода при изменении значений
    global new
    global old
    fl = 0

    new = set_entry.get()

    if old != new:
        old = new
        fl = 1

    if fl:
        answ_line.delete(0, END)


    root.after(50, field_clear)


root = Tk()
root.title('Лабораторная работа №4')
root.geometry('680x400')
root.configure(background='#BEADA1')

root.after(50, field_clear)
old = ''
new = ''

mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label="О программе", command=about_program)
mainmenu.add_command(label="Выйти", command=exit)

# Задание основных параметров
set_label = Label(root, text='Введите координаты точек через пробел', background='#BEADA1', font=('times', 18))
resolve_button = Button(root,  text='Решение', font=('times', 17), command=resolve)
set_entry = Entry(root, width=63, font = '18')
answ_label = Label(root, text='Координаты вершин найденного тругольника:', background='#BEADA1', font=('times', 16))
answ_line = Entry(root, width=70)


# Размещение на экране
set_label.place(x=150, y=10)
set_entry.place(x=20, y=60)
resolve_button.place(x=285, y=110)
answ_label.place(x=135, y=200)
answ_line.place(x=20, y=240)
ans_bis.place(x = 120, y = 280)
bis_line.place(x = 20, y = 320)

root.mainloop()
