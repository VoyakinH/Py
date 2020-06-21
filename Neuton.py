from tkinter import *
from tkinter import messagebox
from math import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Точное значение функции
def f(x):
    #return (x*x) - 4
    #return sin(x)
    #return sin(x) + x*x - 1 + x - x*x + x * 2
    return x - cos(x)


#Первая производная
def f_proizv(x):
    #return 2*x
    return 1 + sin(x)
    #return cos(x)
    #return cos(x) + 2*x + 1 - 2 * x + 2


#Вторая производная
def second_proizv(x):
    #return 2
    return cos(x)
    #return -sin(x)


# Приближённое вычисление корня методом Ньютона

def solution(start, end, eps, max_iter):
    print(start, end)

    answ_diap.append('[' + '{:.2f}'.format(start) + ', ')
    answ_diap.append('{:.2f}'.format(end) + ']')

    if abs(f(start)) < epsil and f(start) * second_proizv(start) > 0:
        numb_iter.append((1))
        y.append(f(start))
        almost_x.append(start)
        error_code.append('0')
        return

    if abs(f(end)) < epsil and f(end) * second_proizv(end) > 0:
        numb_iter.append((1))
        y.append(f(end))
        almost_x.append(end)
        error_code.append('0')
        return

    count_iter = 0
    if (f(end) * f(start)) <= 0:
        flag = 1
        while flag < 3:
            count_iter = 0
            if flag == 1:
                x_n = start
            else:
                x_n = end
            try:
                x_n = x_n - (f(x_n) / f_proizv(x_n))
                x_n_1 = x_n - (f(x_n) / f_proizv(x_n))
            except:
                x_n = end
                x_n = x_n - (f(x_n) / f_proizv(x_n))
                x_n_1 = x_n - (f(x_n) / f_proizv(x_n))
            while abs(x_n - x_n_1) > eps and count_iter < max_iter:
                x_n = x_n_1
                x_n_1 = x_n - (f(x_n) / f_proizv(x_n))
                count_iter += 1
            if start <= x_n_1 <= end:
                break
            flag += 1
    if count_iter >= max_iter:
        error_code.append('1')
        numb_iter.append('-')
        y.append('-')
        almost_x.append('-')
      
    elif x_n_1 < start or x_n_1 > end:
        error_code.append('2')
        numb_iter.append('-')
        y.append('-')
        almost_x.append('-')
    else:
        error_code.append('0')
        numb_iter.append(count_iter)
        y.append(f(x_n_1))
        almost_x.append(x_n_1)
        

        
# Проверка интервала на наличие корней

def check_interval(start, stop):
    if f(start) * f(stop) > 0:
        return 0
    else:
        return 1

def isfloat(s):
    try:
        float(s) 
        return True
    except ValueError:
        return False
# Построение графика

def make_grafik(start, end):
    step = 0.1
    if f(start) < epsil:
        start -= 0.2
    if f(end) < epsil:
        end += 0.2
    end += 0.1
    

    x = np.arange(start, end, step)

    y = []
    for i in x:
       y.append(f(i))

    fig = plt.figure()
    plt.plot(x, y)

    for i in x:
        if f(i - 0.1) < f(i) and f(i + 0.1) < f(i) \
                or f(i - 0.1) > f(i) and f(i + 0.1) > f(i):
             plt.scatter(i, f(i), c='red')

    for i in almost_x:
        if isfloat(i):
            plt.scatter(i, f(i), c='green')

    plt.title('График функции f(x)')
    plt.ylabel('f(x)')
    plt.xlabel('x')

    plt.grid(True)

    plt.show()


# Заполнение таблицы
def make_tabel():
    num = 1
    j = 0
    print(almost_x)
    for i in range(len(almost_x)):
        if (almost_x[i] == '-') and len(almost_x) != 1:
            j+=2
        else:
            if len(almost_x)== 1 or almost_x[i-1] == '-' or(abs(almost_x[i] - almost_x[i-1])>0.0001) or (almost_x[i] * almost_x[i-1] < 0) :
                table[0].insert(END, ''.join(str(num) + '.').center(3))
                num += 1

                table[1].insert(END, ''.join(answ_diap[j] + answ_diap[j + 1]).center(3))
                j += 2

                if error_code[i] == '0':

                    table[2].insert(END, ''.join(str('{:2.4f}'.format(almost_x[i]))).center(12))
                    table[3].insert(END, ''.join(str('{:2.0e}'.format(y[i]))).center(12))
                    table[4].insert(END, ''.join(str(numb_iter[i])).center(12))

                else:
                    table[2].insert(END, '———————'.center(12))
                    table[3].insert(END, '———————'.center(12))
                    table[4].insert(END, '———————'.center(12))

                table[5].insert(END, ''.join(str(error_code[i])).center(12))
            else:
                j+=2


# Поиск интервалов в отрезке
def search():
    try:
        for i in range(6):
            table[i].delete(0, END)
        global error_code
        error_code = []

        global answ_diap
        answ_diap = []

        global almost_x
        almost_x = []

        global y
        y = []

        global numb_iter
        numb_iter = []

        start = float(start_entry.get())
        end = float(end_entry.get())
        step = float(step_entry.get())
        max_iter = float(max_iter_entry.get())
        eps = float(eps_entry.get())
        point_start = start
        point_stop = end
        n = 0

    except:
        messagebox. showerror("Неверный ввод", "Введите данные корректно")
        return

    while point_stop - point_start > epsil:
        if point_start + step > point_stop:
            if check_interval(point_start, point_stop):
                solution(point_start, point_stop, eps, max_iter)
                n += 1
        else:
            if check_interval(point_start, point_start + step):
                solution(point_start, point_start + step, eps, max_iter)
                n += 1

        point_start += step

    if n == 0:
        messagebox.showinfo("Предупреждение", "На данном отрезке нет корней")
    else:
        make_tabel()
        make_grafik(start, end)


# Очистка поля при изменении
def field_clear():  # очистка поля вывода при изменении значений
    global new
    global old
    fl = 0
    new[0] = start_entry.get()
    new[1] = end_entry.get()
    new[2] = step_entry.get()
    new[3] = eps_entry.get()
    new[4] = max_iter_entry.get()

    for i in range(5):
        if old[i] != new[i]:
            old[i] = new[i]
            fl = 1
    if fl:
        for i in range(6):
            table[i].delete(0, END)

    root.after(50, field_clear)


root = Tk()
root.title('Уточнение корней методом Ньютона')
root.geometry('850x450')
root.after(50, field_clear)

new = []
old = []
for i in range(5):
    new.append('')
    old.append('')



const_text = Label(root, font=('times', 12), text='Ввод\n исходных\n данных', bg="#ddddff")
start_text = Label(root, font=('times', 12), text='Начало отрезка', bg="#ddddff", width=15,)
end_text = Label(root, font=('times', 12), text='Конец отрезка', bg="#ddddff", width=15,)
step_text = Label(root, font=('times', 12), text='Шаг',width=15, bg="#ddddff")
eps_text = Label(root, font=('times', 12), text='Точность',  bg="#ddddff", width=15,)
max_iter_text = Label(root, font=('times', 12), text='Число итераций', bg="#ddddff", width=15,)

end_entry = Entry(root, width=15)
step_entry = Entry(root, width=15)
eps_entry = Entry(root, width=15)
max_iter_entry = Entry(root, width=15)
start_entry = Entry(root, width=15)

table_button = Button(root, text='Вычислить', font=('times', 20), bg="#ddddff", height=2, width=40, command=search)


errors = Listbox(root, font=('times', 12), width=40, height=4)
errors.insert(END, "0 - корень нашелся\n")
errors.insert(END, "1 - превышение количества итераций\n")
errors.insert(END, "2 - выход за пределы интервала\n")


num_table = Label(root, text="№", font=('times', 12), bg="#ddddff")
diap_table = Label(root, text="Интервал", font=('times', 12), bg="#ddddff")
ideal_x = Label(root, text="Значение корня", font=('times', 12), bg="#ddddff")
func_of_x = Label(root, text="Значение функции", font=('times', 12), bg="#ddddff")
temp_num_iter = Label(root, text="Число итераций", font=('times', 12), bg="#ddddff")
num_error = Label(root, text="Код ошибки", font=('times', 12), bg="#ddddff")
header_table = Label(root, font=('times', 16), text='Таблица значений', bg="#ddddff", height=1, width=40)
header_error = Label(root, text="Коды ошибок", font=('times', 13), bg="#ddddff")

table = []
for i in range(6):
    table.append(Listbox(root, font=('times', 12), width=20, height=10))

error_code = []
answ_diap = []
almost_x = []
y = []
numb_iter = []
epsil = 0.0000000000000001

# Размещение на экране

const_text.place(x=10, y=30)

start_text.place(x=80, y=30)
start_entry.place(x=80, y=60)

end_text.place(x=230, y=30)
end_entry.place(x=230, y=60)

step_text.place(x=380, y=30)
step_entry.place(x=380, y=60)

eps_text.place(x=530, y=30)
eps_entry.place(x=530, y=60)

max_iter_text.place(x=680, y=30)
max_iter_entry.place(x=680, y=60)

table_button.place(x=350, y=360)

header_table.place(x=220, y=100)

num_table.place(x=10, y=140)
diap_table.place(x=140, y=140)
ideal_x.place(x=270, y=140)
func_of_x.place(x=400, y=140)
temp_num_iter.place(x=530, y=140)
num_error.place(x=660, y=140)

header_error.place(x=20, y=330)
errors.place(x=20, y=360)

temp = 10
for i in range(6):
    table[i].place(x=temp, y=170)
    temp += 130

root.mainloop()