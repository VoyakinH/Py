# Воякин Алексей Янович ИУ7-24Б
# Сортировки

from tkinter import *
from tkinter import messagebox
from random import randint
import timeit


# Очистка поля вывода при изменении поля ввода.
def clr_1():
    sort_ent_2.delete(0, END)
    return True


# Очистка поля ввода по кнопке.
def clr_2(event):
    sort_ent_1.delete(0, END)
    return True


# Очистка поля ввода начального диапазона.
def clr_3():
    diapoz_1.delete(0, END)
    return True


# Очистка поля конечного диапазона.
def clr_4():
    diapoz_2.delete(0, END)
    return True


# Очистка всех полей со временем.
def clr_5():
    slch_n1.delete(0, END)
    slch_n2.delete(0, END)
    slch_n3.delete(0, END)
    ypch_n1.delete(0, END)
    ypch_n2.delete(0, END)
    ypch_n3.delete(0, END)
    ypobch_n1.delete(0, END)
    ypobch_n2.delete(0, END)
    ypobch_n3.delete(0, END)
    sort_n1.delete(0, END)
    sort_n2.delete(0, END)
    sort_n3.delete(0, END)
    return True


# Очистка полей ввода кол-ва чисел по кнопке.
def clr_6(event):
    n1_ent.delete(0, END)
    n2_ent.delete(0, END)
    n3_ent.delete(0, END)
    return 0


# Сортировка выбором для строки чисел через пробел.
def start_sort(event):
    txt = sort_ent_1.get()
    txt = str(txt)
    txt = txt.split(" ")
    for i in range(0, len(txt)):
        try:
            trash = float(txt[i])
        except:
            messagebox.showinfo('Ошибка', "Недопустимые символы")
            return 0
    for i in range(len(txt) - 1):
        m = i
        for j in range(i + 1, len(txt)):
            if float(txt[j]) < float(txt[m]):
                m = j
        txt[m], txt[i] = txt[i], txt[m]
    m = ''
    for i in range(0, len(txt)):
        m += txt[i]
        m += ' '
    sort_ent_2.delete(0, END)
    sort_ent_2.insert(0, m)
    return 0


# Вычисления времени для трёх N.
def count(event):
    n = 1
    ok = count_time(n)
    if ok == 0:
        n = 2
        ok = count_time(n)
        if ok == 0:
            n = 3
            count_time(n)
    return 0


# Вычисление времени.
def count_time(n):
    if n == 1:
        n1 = n1_ent.get()
    if n == 2:
        n1 = n2_ent.get()
    if n == 3:
        n1 = n3_ent.get()
    ok = 0
    try:
        n1 = int(n1)
    except:
        messagebox.showinfo('Ошибка', "Недопустимые символы")
        ok = 1
        return ok
    
    a = diapoz_1.get()
    b = diapoz_2.get()
    global txt_yp
    try:
        a = int(a)
        b = int(b)
    except:
        messagebox.showinfo('Ошибка', "Недопустимые символы")
        ok = 1
        return ok
    if a > b:
        messagebox.showinfo('Ошибка', "Указан неверный интервал значений")
        ok = 1
        return ok
    txt = []
    for i in range(0, n1):
        txt.append(randint(a, b))
    txt_yp = []
    for i in range(0, len(txt)):
        txt_yp.append(txt[i])
        
    time_1 = timeit.timeit("slch(txt_yp)", setup="from __main__ import slch, txt_yp", number=1)
    
    time_2 = timeit.timeit("slch(txt_yp)", setup="from __main__ import slch, txt_yp", number=1)

    txt_yp.sort(reverse=True)
    
    time_3 = timeit.timeit("slch(txt_yp)", setup="from __main__ import slch, txt_yp", number=1)
    
    txt_yp = []
    for i in range(0, len(txt)):
        txt_yp.append(txt[i])
        
    time_4 = timeit.timeit("sort_func(txt_yp)", setup="from __main__ import sort_func, txt_yp", number=1)

    time_1 = '%0.4f' % time_1
    time_2 = '%0.4f' % time_2
    time_3 = '%0.4f' % time_3
    time_4 = '%0.6f' % time_4
    if n == 1 and ok == 0:
        slch_n1.delete(0, END)
        ypch_n1.delete(0, END)
        ypobch_n1.delete(0, END)
        sort_n1.delete(0, END)
        slch_n1.insert(0, time_1)
        ypch_n1.insert(0, time_2)
        ypobch_n1.insert(0, time_3)
        sort_n1.insert(0, time_4)
    if n == 2 and ok == 0:
        slch_n2.delete(0, END)
        ypch_n2.delete(0, END)
        ypobch_n2.delete(0, END)
        sort_n2.delete(0, END)
        slch_n2.insert(0, time_1)
        ypch_n2.insert(0, time_2)
        ypobch_n2.insert(0, time_3)
        sort_n2.insert(0, time_4)
    if n == 3 and ok == 0:
        slch_n3.delete(0, END)
        ypch_n3.delete(0, END)
        ypobch_n3.delete(0, END)
        sort_n3.delete(0, END)
        slch_n3.insert(0, time_1)
        ypch_n3.insert(0, time_2)
        ypobch_n3.insert(0, time_3)
        sort_n3.insert(0, time_4)
    return ok


# Сортировка списка методом выбора.
def slch(txt_yp):
    for i in range(len(txt_yp) - 1):
        m = i
        for j in range(i + 1, len(txt_yp)):
            if float(txt_yp[j]) < float(txt_yp[m]):
                m = j
        txt_yp[m], txt_yp[i] = txt_yp[i], txt_yp[m]


# Сортировка методом sort.
def sort_func(txt_yp):
    txt_yp.sort()


# Main programm
window = Tk()
sv = StringVar()
sv1 = StringVar()
sv2 = StringVar()
sv3 = StringVar()
sv4 = StringVar()
sv5 = StringVar()
window.geometry('850x180')
window.title("Сортировка")
to_sort_1 = Label(window, text="Введите числа для сортировки\nчерез пробел (До 10 чисел)", font=('Arial Bold', 13))
to_sort_2 = Label(window, text="Отсортированный список", font=('Arial Bold', 13))
to_diapoz = Label(window, text="Введите диапазон значений\n для случайного списка", font=('Arial Bold', 13))
to_diapoz_str = Label(window, text=">", font=('Arial Bold', 11))
to_slch = Label(window, text="Случайные числа", font=('Arial Bold', 12))
to_ypch = Label(window, text="Упорядоченные числа", font=('Arial Bold', 12))
to_ypobch = Label(window, text="Упорядоченные числа\n в обратном порядке", font=('Arial Bold', 12))
to_sort = Label(window, text="Функция sort", font=('Arial Bold', 13))
to_n = Label(window, text="Колличество чисел", font=('Arial Bold', 13))
to_info = Label(window, text="Время указывается в секундах", font=('Arial Bold', 13))
sort_ent_1 = Entry(window, textvariable=sv, validate="key", validatecommand=clr_1, width=21)
sort_ent_2 = Entry(window, width=21)
diapoz_1 = Entry(window, textvariable=sv1, validate="all", validatecommand=clr_3, width=6)
diapoz_2 = Entry(window, textvariable=sv2, validate="all", validatecommand=clr_4, width=6)
n1_ent = Entry(window, textvariable=sv3, validate="key", validatecommand=clr_5, width=4)
n2_ent = Entry(window, textvariable=sv4, validate="key", validatecommand=clr_5, width=4)
n3_ent = Entry(window, textvariable=sv5, validate="key", validatecommand=clr_5, width=4)
slch_n1 = Entry(window, width=8)
slch_n2 = Entry(window, width=8)
slch_n3 = Entry(window, width=8)
ypch_n1 = Entry(window, width=8)
ypch_n2 = Entry(window, width=8)
ypch_n3 = Entry(window, width=8)
ypobch_n1 = Entry(window, width=8)
ypobch_n2 = Entry(window, width=8)
ypobch_n3 = Entry(window, width=8)
sort_n1 = Entry(window, width=8)
sort_n2 = Entry(window, width=8)
sort_n3 = Entry(window, width=8)
btn_sort = Button(window, text='Отсортировать', font=('Arial Bold', 13), width=15)
btn_clr = Button(window, text='Очистить', font=('Arial Bold', 13), width=15)
btn_time = Button(window, text='Посчитать время', font=('Arial Bold', 13), width=15)
btn_time_clr = Button(window, text='Очистить', font=('Arial Bold', 13), width=15)
to_info.grid(column=1, row=4, columnspan=3)
to_sort_1.grid(column=0, row=0)
sort_ent_1.grid(column=0, row=1)
to_sort_2.grid(column=0, row=2)
sort_ent_2.grid(column=0, row=3)
btn_sort.grid(column=0, row=4)
btn_clr.grid(column=0, row=5)
to_diapoz.grid(column=1, row=0, columnspan=3)
diapoz_1.grid(column=1, row=1)
to_diapoz_str.grid(column=2, row=1)
diapoz_2.grid(column=3, row=1)
btn_time.grid(column=1, row=2, columnspan=3)
btn_time_clr.grid(column=1, row=3, columnspan=3)
n1_ent.grid(column=5, row=0)
n2_ent.grid(column=6, row=0)
n3_ent.grid(column=7, row=0)
to_n.grid(column=4, row=0)
to_slch.grid(column=4, row=1)
to_ypch.grid(column=4, row=2)
to_ypobch.grid(column=4, row=3)
to_sort.grid(column=4, row=4)
slch_n1.grid(column=5, row=1)
slch_n2.grid(column=6, row=1)
slch_n3.grid(column=7, row=1)
ypch_n1.grid(column=5, row=2)
ypch_n2.grid(column=6, row=2)
ypch_n3.grid(column=7, row=2)
ypobch_n1.grid(column=5, row=3)
ypobch_n2.grid(column=6, row=3)
ypobch_n3.grid(column=7, row=3)
sort_n1.grid(column=5, row=4)
sort_n2.grid(column=6, row=4)
sort_n3.grid(column=7, row=4)
diapoz_1.insert(0, "От")
diapoz_2.insert(0, "До")
btn_sort.bind("<Button-1>", start_sort)
btn_clr.bind("<Button-1>", clr_2)
btn_time_clr.bind("<Button-1>", clr_6)
btn_time.bind("<Button-1>", count)
window.mainloop()
