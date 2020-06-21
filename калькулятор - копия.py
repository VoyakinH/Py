# Воякин Алексей Янович ИУ7-24Б
# Перевод чисел из десятиричной сс в четвиричную и обратно

from tkinter import *
from tkinter import messagebox


# сделать цвет задника в поле ввода белым
def go_white():
    txt['bg'] = 'white'


    
# вычисление из 10 в 4 при нажатии на кнопку 'вычислить'
def output_1(event):
    x = txt.get()
    y1 = x
    val = len(str(x))
    ok = True
    try:
        y = float(x)
        lbl1["text"] = 'Полученное число:'
    except:
        ok = False
        txt['bg'] = 'red'
        window.after(700, go_white)
    if ok:
        k = 0
        if '.' in x:
            y = x.split('.')
            if '-' in y[0]:
                k = 1
                y[0] = y[0][1:]
            x = ''
            y[0] = int(y[0])
            y[1] = int(y[1])
            while y[0] > 0:
                x += str(y[0] % 4)
                y[0] = y[0] // 4
            z = '0.' + str(y[1])
            z = float(z)
            i = spin.get()
            i = int(i)
            j = '.'
            while i > 0:
                z = z * 4
                z = str(z)
                r = z.split('.')
                z = float(z)
                r[0] = int(r[0])
                j += str(r[0])
                z -= r[0]
                i -= 1
        else:
            i = spin.get()
            i = int(i)
            j = '.'
            while i > 0:
                j += '0'
                i -= 1
            x = str(x)
            if '-' in x:
                k = 1
                x = x[1:]
            y = ''
            x = int(x)
            while x > 0:
                y += str(x % 4)
                x = x // 4
            x = y
        if k == 1:
            x += '-'
        if x == '':
            x = 0
            x = str(x)
        x = x[::-1]
        x = str(x)
        x += j
        lbl2['text'] = x
        y2 = txt.get()
        while len(str(y1)) == len(str(y2)):
            y2 = txt.get()
            print(y2)
        lbl1['text'] = ''
        lbl2['text'] = ''


# вычисление из 4 в 10 при нажатии на кнопку 'вычислить'
def output_2(event):
    x = txt.get()
    x = str(x)
    ok = True
    try:
        y = float(x)
    except:
        ok = False
        txt['bg'] = 'red'
        window.after(700, go_white)
    for i in range(len(x)):
        if x[i] in '456789':
            ok = False
            txt['bg'] = 'red'
            window.after(700, go_white)
            break
    if ok:
        lbl1["text"] = 'Полученное число:'
        k = 0
        if '.' in x:
            y = x.split('.')
            y[0] = str(y[0])
            if '-' in y[0]:
                y[0] = y[0][1:]
                k = 1
            y[0] = y[0][::-1]
            st = 1
            j = 0
            for i in range(len(y[0])):
                j += int(y[0][i]) * st
                st *= 4
            st = 1 / 4
            j1 = 0
            for i in range(len(y[1])):
                j1 += int(y[1][i]) * st
                st /= 4
            j2 = str(j1)
            j1 = ''
            x = spin.get()
            for i in range(int(x) + 2):
                if len(j2) > i:
                    j1 += j2[i]
                else:
                    j1 += '0'
            j1 = float(j1)
        else:
            if '-' in x:
                x = x[1:]
                k = 1
            x = x[::-1]
            st = 1
            j = 0
            for i in range(len(x)):
                j += int(x[i]) * st
                st *= 4
            x = spin.get()
            x = int(x)
            j1 = '0.'
            for i in range(x):
                j1 += '0'
            j1 = float(j1)

        if k == 1:
            x = '-'
        else:
            x = ''
        x = x + str(j)
        x = int(x)
        x += j1
        lbl2['text'] = x
        


# Информация о самой программе
def prog_info():
    messagebox.showinfo('Информация', "Данная программа\
 переводит числа четверичной системы счисления в десятичную и обратно.")


# Информация об авторе
def avto_info():
    messagebox.showinfo('Информация', "Разработал Воякин Алексей Янович. Группа ИУ7-24Б,\
 email: aleksei_voyakin@mail.ru")


# Переключение режима на 10 в 4
def switch_1():
    top["text"] = "Перевод из 10-ой в 4-ую"
    lbl["text"] = "Введите число:"
    txt.grid(column=1, row=1)
    lbl3['text'] = "Кол-во зн. поc. зап."
    spin.grid(column=1, row=3, sticky='w')
    btn.grid(columnspan=2)
    btn.bind("<Button-1>", output_1)


# Переключение режима на 4 в 10
def switch_2():
    top["text"] = "Перевод из 4-ой в 10-ую"
    lbl["text"] = "   Введите число:   "
    txt.grid(column=1, row=1)
    lbl3['text'] = "Кол-во зн. поc. зап."
    spin.grid(column=1, row=3, sticky='w')
    btn.grid(columnspan=2)
    btn.bind("<Button-1>", output_2)


# Очистка поля ввода
def clr_1():
    txt.delete(0, END)
    global c
    c = ''


# Очистка поля вывода
def clr_2():
    lbl2['text'] = ''
    lbl1['text'] = ''


# Очистка обоих полей
def clr_all():
    clr_1()
    clr_2()


# Экранная клавиатура
def kboard():
    kb = Tk()
    kb.title("Клавиатура")
    kb.geometry("174x385")
    k1 = Button(kb, text="1", font=("Arial Bold", 30))
    k1.grid(column=0, row=0)
    k2 = Button(kb, text="2", font=("Arial Bold", 30))
    k2.grid(column=1, row=0)
    k3 = Button(kb, text="3", font=("Arial Bold", 30))
    k3.grid(column=2, row=0)
    k4 = Button(kb, text="4", font=("Arial Bold", 30))
    k4.grid(column=0, row=1)
    k5 = Button(kb, text="5", font=("Arial Bold", 30))
    k5.grid(column=1, row=1)
    k6 = Button(kb, text="6", font=("Arial Bold", 30))
    k6.grid(column=2, row=1)
    k7 = Button(kb, text="7", font=("Arial Bold", 30))
    k7.grid(column=0, row=2)
    k8 = Button(kb, text="8", font=("Arial Bold", 30))
    k8.grid(column=1, row=2)
    k9 = Button(kb, text="9", font=("Arial Bold", 30))
    k9.grid(column=2, row=2)
    kt = Button(kb, text=" .", font=("Arial Bold", 30))
    kt.grid(column=0, row=3)
    k0 = Button(kb, text="0", font=("Arial Bold", 30))
    k0.grid(column=1, row=3)
    km = Button(kb, text=" -", font=("Arial Bold", 30))
    km.grid(column=2, row=3)
    kdel = Button(kb, text="Delete", font=("Arial Bold", 30))
    kdel.grid(columnspan=3)
    k1.configure(command=lambda button=Button: output_3('1'))
    k2.configure(command=lambda button=Button: output_3('2'))
    k3.configure(command=lambda button=Button: output_3('3'))
    k4.configure(command=lambda button=Button: output_3('4'))
    k5.configure(command=lambda button=Button: output_3('5'))
    k6.configure(command=lambda button=Button: output_3('6'))
    k7.configure(command=lambda button=Button: output_3('7'))
    k8.configure(command=lambda button=Button: output_3('8'))
    k9.configure(command=lambda button=Button: output_3('9'))
    k0.configure(command=lambda button=Button: output_3('0'))
    kt.configure(command=lambda button=Button: output_3('.'))
    km.configure(command=lambda button=Button: output_3('-'))
    kdel.bind("<Button-1>", output_4)
    kb.mainloop()


# Нажатие по клавиатуре
def output_3(s):
    global c
    c += s
    txt.delete(0, END)
    txt.insert(0, c)


#Удаление символа
def output_4(event):
    global c
    c = c[:-1]
    txt.delete(0, END)
    txt.insert(0, c)
    
# Задание и расположение виджетов в окне программы
window = Tk()
c = ''
menu = Menu(window)
item1 = Menu(menu, tearoff=0)
item1.add_command(label='10-ая -> 4-ая', command=switch_1)
item1.add_command(label='4-ая -> 10-ая', command=switch_2)
menu.add_cascade(label='Действия', menu=item1)
item2 = Menu(menu, tearoff=0)
item2.add_command(label='Очистить поле ввода', command=clr_1)
item2.add_command(label='Очистить поле вывода', command=clr_2)
item2.add_command(label='Очистить оба поля', command=clr_all)
menu.add_cascade(label='Очистка', menu=item2)
item3 = Menu(menu, tearoff=0)
item3.add_command(label='О программе', command=prog_info)
item3.add_command(label='Об авторе', command=avto_info)
menu.add_cascade(label='Информация', menu=item3)
item4 = Menu(menu, tearoff=0)
item4.add_command(label="Открыть экранную клавиатуру", command=kboard)
menu.add_cascade(label="Клавиатура", menu=item4)

window.config(menu=menu)

window.geometry('380x170')
window.title("Калькулятор")
top = Label(window, text="Выберите режим перевода", font=('Arial Bold', 20))
top.grid(columnspan=2)
lbl = Label(window, font=('Arial Bold', 16))
lbl.grid(column=0, row=1, sticky='w')

txt = Entry(window, width=30)

spin = Spinbox(window, from_=1, to=7, width=5)
btn = Button(window, text='Перевести', font=('Arial Bold', 12))
lbl1 = Label(window, font=('Arial Bold', 16))
lbl1.grid(column=0, row=4)
lbl2 = Label(window, font=('Arial Bold', 16))
lbl2.grid(column=1, row=4)
lbl3 = Label(window, font=('Arial Bold', 16))
lbl3.grid(column=0, row=3)
window.mainloop()
