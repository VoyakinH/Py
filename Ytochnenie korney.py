# Воякин Алексей Янович ИУ7-24Б

from tkinter import *
import tkinter.messagebox as mb
import matplotlib
from math import *
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


def f(x):
    return x*x-4


def fi_f(x):
    if 2 * x == 0:
        l = 1 / (2*(x - 0.1))
    else:
        l = 1 / (2*x)

    return x - l * f(x)


def scroll(*args):
    Lb1.yview(*args)
    Lb2.yview(*args)
    Lb3.yview(*args)
    Lb4.yview(*args)
    Lb5.yview(*args)
    Lb6.yview(*args)


def root_search_point(a, eps, n):
    i = 0
    xpr = a
    while i < n:
        i += 1
        fi = fi_f(xpr)
        x = fi
        if abs(x - xpr) < eps:
            return x, i, 0
        xpr = x
    return 10 * '-', i, 1


def root_search(a, b, eps, n):
    i2 = i3 = 0
    x, i1, code = root_search_point(a, eps, n)
    if code != 0 or x > b or x < a:
        x, i2, code = root_search_point(b, eps, n)
    if code != 0 or x > b or x < a:
        x, i3, code = root_search_point(a + b / 2, eps, n)
    i = i1 + i2 + i3
    if code == 0 and (x > b or x < a):
        x, i, code = chast(a, b, eps, n)

    return x, i, code


def chast(x2, x1, e, n):
    print("da")
    k=0
    t = x2
    y = x1
    '''
    if y >= b:
        y = b
    if x1 >= b:
        x1 = b
    '''
    while abs(x2 - x1) > e:
            x0 = x1
            x1 = x2
            x2 = x1 - ((x0 - x1) * f(x1)) / (f(x0) - f(x1))
            print('x2   ',x2)
            k += 1
            if k >= n:
                x2 = 10*'-'
                code = 1
                break
    if y >= x2 >= t:
        if int(x2) == 0:
            x2 = int(x2)
        else:
            x2 = round(x2, 5)
            code = 0
    return x2, k, code


def solution(a, b, eps, h, n):
    c1 = a
    c2 = a
    k = 0
    while c2 < b:
        found = True
        x_sol = 0
        y_sol = 0
        err_code = 0
        n_iter = 1

        c2 += h
        if c2 > b:
            c2 = b
        if abs(f(c1)) <= 1e-10:
            x_sol = c1
            y_sol = f(c1)
        elif abs(f(c2)) <= 1e-10:
            if c2 == b:
                x_sol = c2
                y_sol = f(c2)
            else:
                found = False
        elif f(c1) * f(c2) < 0:
            x_sol, n_iter, err_code = root_search(c1, c2, eps, n)
            if err_code == 0:
                y_sol = f(x_sol)
        else:
            found = False

        if found:
            k += 1
            print("{:3d}".format(k), end=' ')
            t['n'].append(k)
            print("[{:10.7f};{:10.7f}]".format(c1, c2), end=' ')
            t['ab'].append([(round(c1, 8)), (round(c2, 8))])
            if err_code == 0:
                print("{:10.7f}".format(x_sol), end=' ')
                print("{:10.7f}".format(y_sol), end=' ')
                t['y'].append(y_sol)
                t['x'].append(x_sol)
            else:
                print(10 * '-', end=' ')
                print(10 * '-', end=' ')
                t['x'].append(12 * '-')
                t['y'].append(12 * '-')
            print("{:8d}".format(n_iter), end=' ')
            t['N'].append(n_iter)
            print("{:10d}".format(err_code))
            t['err'].append(err_code)
        c1 = c2


def main():
    Lb1.delete(0, END)
    Lb2.delete(0, END)
    Lb3.delete(0, END)
    Lb4.delete(0, END)
    Lb5.delete(0, END)
    Lb6.delete(0, END)
    flag = 0
    try:
        a = float(E1.get())
        b = float(E2.get())
        step = float(E3.get())
        eps = float(E4.get())
        n = float(E5.get())
        flag = 1
    except:
        mb.showerror("Неверный ввод", "Введите действительные числа в поля ввода")
    if flag == 1:
        t['n'], t['ab'], t['x'], t['y'], \
        t['N'], t['err'] = [], [], [], [], [], []
        a1, b1 = a, b
        num = 0
        while a < b:
            if f(a) == 0 and num != 0:
                num -= 1
            else:
                if (a + step) > b:
                    solution(a, b, eps, step, n)
                else:
                    solution(a, a + step, eps, step, n)
            a += step
            num += 1
        n = len(t['n'])
        i = 0
        while i < (n - 1):
            if str(t['x'][i]) != 12 * '-' and str(t['x'][i + 1]) != 12 * '-':
                if abs(t['x'][i] - t['x'][i + 1]) <= eps:
                    t['ab'].pop(i)
                    t['err'].pop(i)
                    t['n'].pop(i)
                    t['x'].pop(i)
                    t['y'].pop(i)
                    t['N'].pop(i)
                    n -= 1
                    i -= 1
            i += 1
        if t['n'] == []:
            mb.showerror("Ошибка!", 'Нет корней на [' + \
                         str(a1) + '; ' + str(b1) + ']')
        num = 1
        for i in range(len(t['n'])):
            Lb1.insert(END, ''.join(str(num) + '.').center(3))
            num += 1
            Lb2.insert(END, ''.join(str(t['ab'][i]).center(12)))
            try:
                print(str(t['x'][i]))
                if (12 * '-') == str(t['x'][i]):
                    print('!!!')
                    Lb3.insert(END, ''.join())  \
                        ('{:g}'.format(t['x'][i]).center(12))
                else:
                    Lb3.insert(END, ''.join('{:g}'.format(t['x'][i]).center(13)))
                if (12 * '-') == str(t['y'][i]):
                    Lb4.insert(END, ''.join('{:1.0e}'.format(t['y'][i]).center(12)))
                else:
                    Lb4.insert(END, ''.join('{:1.0e}'.format\
                                                (t['y'][i]).center(13)))
            except:
                Lb3.insert(END, ''.join(t['x'][i]).center(14))
                Lb4.insert(END, ''.join(t['y'][i]).center(14))

            Lb5.insert(END, ''.join(str(t['N'][i]).center(18)))
            Lb6.insert(END, ''.join(str(t['err'][i]).center(18)))
        x = []
        y = []
        x_e = []
        y_e = []
        x0 = []
        y0 = []
        while a1 < b1:
            if f(a1 - 0.001) < f(a1) and f(a1 + 0.001) < f(a1) \
                    or f(a1 - 0.001) > f(a1) \
                    and f(a1 + 0.001) > f(a1):
                x_e.append(a1)
                y_e.append(f(a1))
            if f(a1 - 0.001) < 0 and f(a1 + 0.001) > 0 or f(a1 - 0.001) > 0 and f(a1 + 0.001) < 0:
                x0.append(a1)
                y0.append(f(a1))
                a += 0.01
            elif abs(round(float('{:g}'.format(f(a1))), 6)) == 0:
                x0.append(a1)
                y0.append(f(a1))
                a += 0.01
            x.append(a1)
            y.append(f(a1))
            a1 += 0.001
        y_oy = [0, 0]
        if min(y) < 0:
            y_oy[0] = min(y)
        else:
            y_oy[0] = -0.5
        if max(y) > 0:
            y_oy[1] = max(y)
        else:
            y_oy[1] = 0.5
        plt.clf()
        plt.plot(x, y)
        plt.scatter(x_e, y_e, color='blue')
        plt.scatter(x0, y0, color='red')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        plt.show()


# Main program
t = {'n': [], 'ab': [], 'x': [], 'y': [], 'N': [], 'err': []}
window = Tk()
window.geometry('900x350')
window.title("Уточнение корней")
Fm = Frame(window)
Sb = Scrollbar(window, command=scroll)

Lab0 = Label(window, font=('Arial Bold', 12), text='Ввод констант', width=15, bg="white")
Lab1 = Label(window, font=('Arial Bold', 12), text='Начало отрезка', width=15, bg="white")
Lab2 = Label(window, font=('Arial Bold', 12), text='Конец отрезка', width=15, bg="white")
Lab3 = Label(window, font=('Arial Bold', 12), text='Шаг', width=15, bg="white")
Lab4 = Label(window, font=('Arial Bold', 12), text='Точность', width=15, bg="white")
Lab5 = Label(window, font=('Arial Bold', 12), text='Число итераций', width=15, bg="white")

LabTb0 = Label(window, font=('Arial Bold', 12), text='Номер', width=15, bg="white")
LabTb1 = Label(window, font=('Arial Bold', 12), text='Интервал', width=15, bg="white")
LabTb2 = Label(window, font=('Arial Bold', 12), text='Значение корня', width=15, bg="white")
LabTb3 = Label(window, font=('Arial Bold', 12), text='Значение функции', width=15, bg="white")
LabTb4 = Label(window, font=('Arial Bold', 12), text='№ итерации', width=15, bg="white")

E1 = Entry(window, width=15, bg="white")
E2 = Entry(window, width=15, bg="white")
E3 = Entry(window, width=15, bg="white")
E4 = Entry(window, width=15, bg="white")
E5 = Entry(window, width=15, bg="white")

B = Button(window, text='Вычислить', font=('times', 20), command=main)

Lb1 = Listbox(window, font=('Arial Bold', 12), width=20, height=10, yscrollcommand=Sb.set, bg="white")
Lb2 = Listbox(window, font=('Arial Bold', 12), width=20, height=10, yscrollcommand=Sb.set, bg="white")
Lb3 = Listbox(window, font=('Arial Bold', 12), width=20, height=10, yscrollcommand=Sb.set, bg="white")
Lb4 = Listbox(window, font=('Arial Bold', 12), width=20, height=10, yscrollcommand=Sb.set, bg="white")
Lb5 = Listbox(window, font=('Arial Bold', 12), width=20, height=10, yscrollcommand=Sb.set, bg="white")
Lb6 = Listbox(window, font=('Arial Bold', 12), width=20, height=10, yscrollcommand=Sb.set, bg="white")

Lb7 = Listbox(window, font=('Arial Bold', 12), width=40, height=4, bg="white")
Lb7.insert(END, "0 - корень нашелся\n")
Lb7.insert(END, "1 - превышение количества итераций\n")
Lb7.insert(END, "2 - выход за пределы интервала\n")

Lab11 = Label(window, text="№", font=('Arial Bold', 12),  bg="white")
Lab12 = Label(window, text="Интервал", font=('Arial Bold', 12), bg="white")
Lab13 = Label(window, text="Значение корня", font=('Arial Bold', 12),  bg="white")
Lab14 = Label(window, text="Значение функции", font=('Arial Bold', 12), bg="white")
Lab15 = Label(window, text="№ итерации", font=('Arial Bold', 12), bg="white")
Lab16 = Label(window, text="Код ошибки", font=('Arial Bold',  12), bg="white")
Labtit = Label(window, font=('Arial Bold', 14), text='Таблица значений',  bg="white")
Lab20 = Label(window, text="Коды ошибок",  font=('Arial Bold', 13), bg="white")

Lab1.grid(row=0, column=1)
Lab2.grid(row=0, column=2)
Lab3.grid(row=0, column=3)
Lab4.grid(row=0, column=4)
Lab5.grid(row=0, column=5)

Lab0.grid(row=1, column=0)
E1.grid(row=1, column=1)
E2.grid(row=1, column=2)
E3.grid(row=1, column=3)
E4.grid(row=1, column=4)
E5.grid(row=1, column=5)
B.grid(row=7, column=3)

Labtit.grid(row=3, column=0, columnspan=6)

Lab11.grid(row=4, column=0)
Lab12.grid(row=4, column=1)
Lab13.grid(row=4, column=2)
Lab14.grid(row=4, column=3)
Lab15.grid(row=4, column=4)
Lab16.grid(row=4, column=5)

Lb1.grid(row=5, column=0)
Lb2.grid(row=5, column=1)
Lb3.grid(row=5, column=2)
Lb4.grid(row=5, column=3)
Lb5.grid(row=5, column=4)
Lb6.grid(row=5, column=5)
Sb.grid(row=5, column=6, sticky=S+N)

Lab20.grid(row=6, column=0, columnspan=2)
Lb7.grid(row=7, column=0, columnspan=2)
window.mainloop()
