# Воякин Алексей Янович ИУ7-24Б
# Защита сортировки со  временем
from tkinter import *


def clr_1():
    sort_ent_2.delete(0, END)
    return True


def clr_2(event):
    sort_ent_1.delete(0, END)
    return


def start_sort(event):
    clr_2
    x = sort_ent_1.get()
    x = x.split(" ")
    first = 0
    last = len(x) - 1
    x = fast_sort(x, first, last)
    sort_ent_2.insert(0, x)
    return


def fast_sort(x, first, last):
    if first >= last:
        return 0
    l = first
    r = last
    a = x[(l + r) // 2]
    while l < r:
        while l <= last and x[l] <= a:
            l += 1
        while r >= first and x[r] >= a:
            r -= 1
        if l < r:
            x[l], x[r] = x[r], x[l]
            l += 1
            r -= 1
    fast_sort(x, first, r)
    fast_sort(x, l, last)
    return x


window = Tk()
sv = StringVar()
to_sort_1 = Label(window, text="Введите числа для сортировки\nчерез пробел (До 10 чисел)", font=('Arial Bold', 13))
to_sort_2 = Label(window, text="Отсортированный список", font=('Arial Bold', 13))
sort_ent_1 = Entry(window, textvariable=sv, validate="key", validatecommand=clr_1, width=21)
sort_ent_2 = Entry(window, width=21)
btn_sort = Button(window, text='Отсортировать', font=('Arial Bold', 13), width=15)
btn_clr = Button(window, text='Очистить', font=('Arial Bold', 13), width=15)
to_sort_1.grid(column=0, row=0)
sort_ent_1.grid(column=0, row=1)
to_sort_2.grid(column=0, row=2)
sort_ent_2.grid(column=0, row=3)
btn_sort.grid(column=0, row=4)
btn_clr.grid(column=0, row=5)
btn_sort.bind("<Button-1>", start_sort)
btn_clr.bind("<Button-1>", clr_2)
window.mainloop()