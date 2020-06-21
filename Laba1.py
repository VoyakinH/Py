from tkinter import *
from tkinter import messagebox

digit_list = ('0', '1', '2', '3', '.', '-')


def info_click():           # Функция вкладки информация
    messagebox.showinfo("Info", "Трунцев Георгий ИУ7-24Б \nEmail: joraxorosh@gmail.com\nПрограмма складывает или вычитает дробные и целые, отрицательные и положительные числа в четверичной системе счисления.")


def push1(event):
    digit1.insert(END, "0")
    return 0


def push2(event):
    digit1.insert(END, "1")
    return 0


def push3(event):
    digit1.insert(END, "2")
    return 0


def push4(event):
    digit1.insert(END, "3")
    return 0


def push5(event):
    digit2.insert(END, "0")
    return 0


def push6(event):
    digit2.insert(END, "1")
    return 0


def push7(event):
    digit2.insert(END, "2")
    return 0


def push8(event):
    digit2.insert(END, "3")
    return 0


def push9(event):
    digit1.insert(END, ".")
    return 0


def push10(event):
    digit2.insert(END, ".")
    return 0


def push11(event):
    digit1.insert(END, "-")
    return 0


def push12(event):
    digit2.insert(END, "-")
    return 0


def chist1():
    digit1.delete(0, END)
    return 0


def chist2():
    digit2.delete(0, END)
    return 0


def chist3():
    label2.config(text="")
    return 0


def chist4():
    digit1.delete(0, END)
    digit2.delete(0, END)
    label2.config(text="")
    return 0


def check_digits():             # Проверка ввода
    ct = 0
    s = ''
    s = digit1.get()
    if s == '' or s[len(s)-1] == '.' or s[0] == '.' or ((s[0] == '-') and (s[1] == '.')):
        return 0

    for i in range(0, len(s), 1):
        if s[i] == '.':
            ct += 1
        if s[i] == '-' and i != 0:
            return 0
        if (ct > 1) or (not(s[i] in digit_list)):
            return 0
    s = digit2.get()
    ct = 0
    if s == '' or s[len(s)-1] == '.' or s[0] == '.' or ((s[0] == '-') and (s[1] == '.')):
        return 0
    for i in range(0, len(s), 1):
        if s[i] == '.':
            ct += 1
        if s[i] == '-' and i != 0:
            return 0
        if (ct > 1) or (not (s[i] in digit_list)):
            return 0
    return 1


def do_schet(a, b):
    if a[0] == '-':
        i = 1
        while a[i] == '0' and not((i + 2 > len(a) - 1) or (a[i + 1] == '.')):
            a = a[:i] + a[i + 1:]
    else:
        i = 0
        while a[i] == '0' and not((i + 2 > len(a) - 1) or (a[i + 1] == '.')):
            a = a[:i] + a[i + 1:]
    if b[0] == '-':
        i = 1
        while b[i] == '0' and not((i + 2 > len(b) - 1) or (b[i + 1] == '.')):
            b = b[:i] + b[i + 1:]
    else:
        i = 0
        while b[i] == '0' and not((i + 2 > len(b) - 1) or (b[i + 1] == '.')):
            b = b[:i] + b[i + 1:]
    digit1.delete(0, END)
    digit1.insert(0, a)
    digit2.delete(0, END)
    digit2.insert(0, b)
    a = a.split('.')
    b = b.split('.')
    print(a, '  ', b)
    if len(a) == 2 and len(b) == 1:             # Делаем количество цифр в числах одинаковым до и после запятой
        b.append('')
        b[1] = '0' * len(a[1])
    if len(b) == 2 and len(a) == 1:
        a.append('')
        a[1] = '0' * len(b[1])
    if len(a) > 1:
        if len(a[1]) > len(b[1]):
            b[1] = b[1] + '0' * (len(a[1]) - len(b[1]))
        else:
            a[1] = a[1] + '0' * (len(b[1]) - len(a[1]))
    print(a, '  ', b)
    if lang.get() == 1:                             # Сложение
        if a[0][0] == '-' and b[0][0] == '-':           # Случай сложения двух отрицательных чисел
            if len(a[0]) > len(b[0]):
                b[0] = b[0][0] + '0' * (len(a[0]) - len(b[0])) + b[0][1:]
            else:
                a[0] = a[0][0] + '0' * (len(b[0]) - len(a[0])) + a[0][1:]
            ost = 0
            s = ['']
            if len(a) == 2:
                s.append('')
                for i in range(len(a[1]) - 1, -1, -1):
                    s[1] = str((int(a[1][i]) + int(b[1][i]) + ost) % 4) + s[1]
                    ost = (int(a[1][i]) + int(b[1][i]) + ost) // 4
                    print(ost)
            for i in range(len(a[0]) - 1, 0, -1):
                s[0] = str(((int(a[0][i]) + int(b[0][i])) + ost) % 4) + s[0]
                ost = ((int(a[0][i]) + int(b[0][i])) + ost) // 4
                print(ost)
            if ost != 0:
                s[0] = '-' + str(ost) + s[0]
            else:
                s[0] = '-' + s[0]
            print(a, '  ', b, ' result: ', s)
            print('-----------------------------------')
            s = s[0] + '.' + s[1]
            label2.config(text=s)
        if a[0][0] != '-' and b[0][0] != '-':           # Случай сложения двух положительных чисел
            if len(a[0]) > len(b[0]):
                b[0] = '0' * (len(a[0]) - len(b[0])) + b[0]
            else:
                a[0] = '0' * (len(b[0]) - len(a[0])) + a[0]
            ost = 0
            s = ['']
            if len(a) == 2:
                s.append('')
                for i in range(len(a[1]) - 1, -1, -1):
                    s[1] = str((int(a[1][i]) + int(b[1][i]) + ost) % 4) + s[1]
                    ost = (int(a[1][i]) + int(b[1][i]) + ost) // 4
                    print(ost)
            for i in range(len(a[0]) - 1, -1, -1):
                s[0] = str(((int(a[0][i]) + int(b[0][i])) + ost) % 4) + s[0]
                ost = ((int(a[0][i]) + int(b[0][i])) + ost) // 4
                print(ost)
            if ost != 0:
                s[0] = str(ost) + s[0]
            print(a, '  ', b, ' result: ', s)
            print('-----------------------------------')
            s = s[0] + '.' + s[1]
            label2.config(text=s)
        if (a[0][0] == '-' and b[0][0] != '-') or (b[0][0] == '-' and a[0][0] != '-'):          # Случай сложения отрицателного и положительного числа
            if b[0][0] == '-' and a[0][0] != '-':
                a, b = b, a
            if len(a) > 1:                # Находим максимальное из чисел по модулю
                a1 = a[0] + a[1]
                b1 = b[0] + b[1]
            else:
                a1 = a[0]
                b1 = b[0]
            if abs(int(a1)) > int(b1):                  # Случай если отрицательное больше положительного
                a[0] = a[0][1:]
                s = ['']
                if len(a) == 2:
                    s.append('')
                    for i in range(len(a[1]) - 1, -1, -1):
                        if (a[1][i] == 'f') or int(a[1][i]) < int(b[1][i]):
                            if a[1][i] == 'f':
                                a[1] = a[1][:i] + '3' + a[1][(i + 1):]
                            else:
                                a[1] = a[1][:i] + str(int(a[1][i]) + 4) + a[1][(i + 1):]
                            if i == 0:
                                if str(int(a[0][len(a) - 1]) - 1) == '-1':
                                    a[0] = a[0][:(len(a[0]) - 1)] + 'f'
                                else:
                                    a[0] = a[0][:(len(a[0]) - 1)] + str(int(a[0][len(a) - 1]) - 1)
                            else:
                                if str(int(a[1][i - 1]) - 1) == '-1':
                                    a[1] = a[1][:(i - 1)] + 'f' + a[1][i:]
                                else:
                                    a[1] = a[1][:(i - 1)] + str(int(a[1][i - 1]) - 1) + a[1][i:]
                        print(a)
                        s[1] = str(int(a[1][i]) - int(b[1][i])) + s[1]
                for i in range(len(a[0]) - 1, -1, -1):
                    if (a[0][i] == 'f') or (int(a[0][i]) < int(b[0][i])):
                        if a[0][i] == 'f':
                            a[0] = a[0][:i] + '3' + a[0][(i + 1):]
                        else:
                            a[0] = a[0][:i] + str(int(a[0][i]) + 4) + a[0][(i + 1):]
                        if str(int(a[0][i - 1]) - 1) == '-1':
                            a[0] = a[0][:(i - 1)] + 'f' + a[0][i:]
                        else:
                            a[0] = a[0][:(i - 1)] + str(int(a[0][i - 1]) - 1) + a[0][i:]
                    print(a)
                    s[0] = str(int(a[0][i]) - int(b[0][i])) + s[0]
                s[0] = '-' + s[0]
                print(a, '  ', b, ' result: ', s)
                print('-----------------------------------')
                s = s[0] + '.' + s[1]
                a[0] = '-' + a[0]
                label2.config(text=s)
            else:
                a[0] = a[0][1:]                         # Случай если положительное больше отрицательного при вычитании
                s = ['']
                if len(b) == 2:
                    s.append('')
                    for i in range(len(b[1]) - 1, -1, -1):
                        if (b[1][i] == 'f') or int(b[1][i]) < int(a[1][i]):
                            if b[1][i] == 'f':
                                b[1] = b[1][:i] + '3' + b[1][(i + 1):]
                            else:
                                b[1] = b[1][:i] + str(int(b[1][i]) + 4) + b[1][(i + 1):]
                            if i == 0:
                                if str(int(b[0][len(b) - 1]) - 1) == '-1':
                                    b[0] = b[0][:(len(b[0]) - 1)] + 'f'
                                else:
                                    b[0] = b[0][:(len(b[0]) - 1)] + str(int(b[0][len(b) - 1]) - 1)
                            else:
                                if str(int(b[1][i - 1]) - 1) == '-1':
                                    b[1] = b[1][:(i - 1)] + 'f' + b[1][i:]
                                else:
                                    b[1] = b[1][:(i - 1)] + str(int(b[1][i - 1]) - 1) + b[1][i:]
                        print(b)
                        s[1] = str(int(b[1][i]) - int(a[1][i])) + s[1]
                for i in range(len(b[0]) - 1, -1, -1):
                    if (b[0][i] == 'f') or (int(b[0][i]) < int(a[0][i])):
                        if b[0][i] == 'f':
                            b[0] = b[0][:i] + '3' + b[0][(i + 1):]
                        else:
                            b[0] = b[0][:i] + str(int(b[0][i]) + 4) + b[0][(i + 1):]
                        if str(int(b[0][i - 1]) - 1) == '-1':
                            b[0] = b[0][:(i - 1)] + 'f' + b[0][i:]
                        else:
                            b[0] = b[0][:(i - 1)] + str(int(b[0][i - 1]) - 1) + b[0][i:]
                    print(b)
                    s[0] = str(int(b[0][i]) - int(a[0][i])) + s[0]
                print(b, '  ', a, ' result: ', s)
                print('-----------------------------------')
                s = s[0] + '.' + s[1]
                a[0] = '-' + a[0]
                label2.config(text=s)
    else:
        print('Вычитание')
        if a[0][0] == '-' and b[0][0] == '-':           # Случай вычитания отрицательных
            if len(a) > 1:                # Находим максимальное из чисел по модулю
                a1 = a[0] + a[1]
                b1 = b[0] + b[1]
            else:
                a1 = a[0]
                b1 = b[0]
            if abs(int(a1)) > abs(int(b1)):                  # Случай если отрицательное больше положительного
                a[0] = a[0][1:]
                b[0] = b[0][1:]
                s = ['']
                if len(a) == 2:
                    s.append('')
                    for i in range(len(a[1]) - 1, -1, -1):
                        if (a[1][i] == 'f') or int(a[1][i]) < int(b[1][i]):
                            if a[1][i] == 'f':
                                a[1] = a[1][:i] + '3' + a[1][(i + 1):]
                            else:
                                a[1] = a[1][:i] + str(int(a[1][i]) + 4) + a[1][(i + 1):]
                            if i == 0:
                                if str(int(a[0][len(a) - 1]) - 1) == '-1':
                                    a[0] = a[0][:(len(a[0]) - 1)] + 'f'
                                else:
                                    a[0] = a[0][:(len(a[0]) - 1)] + str(int(a[0][len(a) - 1]) - 1)
                            else:
                                if str(int(a[1][i - 1]) - 1) == '-1':
                                    a[1] = a[1][:(i - 1)] + 'f' + a[1][i:]
                                else:
                                    a[1] = a[1][:(i - 1)] + str(int(a[1][i - 1]) - 1) + a[1][i:]
                        print(a)
                        s[1] = str(int(a[1][i]) - int(b[1][i])) + s[1]
                for i in range(len(a[0]) - 1, -1, -1):
                    if (a[0][i] == 'f') or (int(a[0][i]) < int(b[0][i])):
                        if a[0][i] == 'f':
                            a[0] = a[0][:i] + '3' + a[0][(i + 1):]
                        else:
                            a[0] = a[0][:i] + str(int(a[0][i]) + 4) + a[0][(i + 1):]
                        if str(int(a[0][i - 1]) - 1) == '-1':
                            a[0] = a[0][:(i - 1)] + 'f' + a[0][i:]
                        else:
                            a[0] = a[0][:(i - 1)] + str(int(a[0][i - 1]) - 1) + a[0][i:]
                    print(a)
                    s[0] = str(int(a[0][i]) - int(b[0][i])) + s[0]
                s[0] = '-' + s[0]
                print(a, '  ', b, ' result: ', s)
                print('-----------------------------------')
                s = s[0] + '.' + s[1]
                a[0] = '-' + a[0]
                b[0] = '-' + b[0]
                label2.config(text=s)
            else:
                a[0] = a[0][1:]
                b[0] = b[0][1:]                             # Случай если 2 число больше при вычитании
                s = ['']
                if len(b) == 2:
                    s.append('')
                    for i in range(len(b[1]) - 1, -1, -1):
                        if (b[1][i] == 'f') or int(b[1][i]) < int(a[1][i]):
                            if b[1][i] == 'f':
                                b[1] = b[1][:i] + '3' + b[1][(i + 1):]
                            else:
                                b[1] = b[1][:i] + str(int(b[1][i]) + 4) + b[1][(i + 1):]
                            if i == 0:
                                if str(int(b[0][len(b) - 1]) - 1) == '-1':
                                    b[0] = b[0][:(len(b[0]) - 1)] + 'f'
                                else:
                                    b[0] = b[0][:(len(b[0]) - 1)] + str(int(b[0][len(b) - 1]) - 1)
                            else:
                                if str(int(b[1][i - 1]) - 1) == '-1':
                                    b[1] = b[1][:(i - 1)] + 'f' + b[1][i:]
                                else:
                                    b[1] = b[1][:(i - 1)] + str(int(b[1][i - 1]) - 1) + b[1][i:]
                        print(b)
                        s[1] = str(int(b[1][i]) - int(a[1][i])) + s[1]
                for i in range(len(b[0]) - 1, -1, -1):
                    if (b[0][i] == 'f') or (int(b[0][i]) < int(a[0][i])):
                        if b[0][i] == 'f':
                            b[0] = b[0][:i] + '3' + b[0][(i + 1):]
                        else:
                            b[0] = b[0][:i] + str(int(b[0][i]) + 4) + b[0][(i + 1):]
                        if str(int(b[0][i - 1]) - 1) == '-1':
                            b[0] = b[0][:(i - 1)] + 'f' + b[0][i:]
                        else:
                            b[0] = b[0][:(i - 1)] + str(int(b[0][i - 1]) - 1) + b[0][i:]
                    print(b)
                    s[0] = str(int(b[0][i]) - int(a[0][i])) + s[0]
                print(b, '  ', a, ' result: ', s)
                print('-----------------------------------')
                s = s[0] + '.' + s[1]
                a[0] = '-' + a[0]
                b[0] = '-' + b[0]
                label2.config(text=s)
        if a[0][0] == '-' and b[0][0] != '-':               # Случай вычетания отрацительного и положительного числа
            a[0] = a[0][1:]
            if len(a[0]) > len(b[0]):
                b[0] = '0' * (len(a[0]) - len(b[0])) + b[0]
            else:
                a[0] = '0' * (len(b[0]) - len(a[0])) + a[0]
            ost = 0
            s = ['']
            if len(a) == 2:
                s.append('')
                for i in range(len(a[1]) - 1, -1, -1):
                    s[1] = str((int(a[1][i]) + int(b[1][i]) + ost) % 4) + s[1]
                    ost = (int(a[1][i]) + int(b[1][i]) + ost) // 4
                    print(ost)
            for i in range(len(a[0]) - 1, -1, -1):
                s[0] = str(((int(a[0][i]) + int(b[0][i])) + ost) % 4) + s[0]
                ost = ((int(a[0][i]) + int(b[0][i])) + ost) // 4
                print(ost)
            if ost != 0:
                s[0] = str(ost) + s[0]

            print(a, '  ', b, ' result: ', s)
            print('-----------------------------------')
            s = '-' + s[0] + '.' + s[1]
            a[0] = '-' + a[0]
            label2.config(text=s)
        if a[0][0] != '-' and b[0][0] == '-':               # Случай вычитания положительного и отрицательного
            b[0] = b[0][1:]
            if len(a[0]) > len(b[0]):
                b[0] = '0' * (len(a[0]) - len(b[0])) + b[0]
            else:
                a[0] = '0' * (len(b[0]) - len(a[0])) + a[0]
            ost = 0
            s = ['']
            if len(a) == 2:
                s.append('')
                for i in range(len(a[1]) - 1, -1, -1):
                    s[1] = str((int(a[1][i]) + int(b[1][i]) + ost) % 4) + s[1]
                    ost = (int(a[1][i]) + int(b[1][i]) + ost) // 4
                    print(ost)
            for i in range(len(a[0]) - 1, -1, -1):
                s[0] = str(((int(a[0][i]) + int(b[0][i])) + ost) % 4) + s[0]
                ost = ((int(a[0][i]) + int(b[0][i])) + ost) // 4
                print(ost)
            if ost != 0:
                s[0] = str(ost) + s[0]
            print(a, '  ', b, ' result: ', s)
            print('-----------------------------------')
            s = s[0] + '.' + s[1]
            b[0] = '-' + b[0]
            label2.config(text=s)
        if a[0][0] != '-' and b[0][0] != '-':                   # Случай вычетания положительных
            if len(a) > 1:                # Находим максимальное из чисел по модулю
                a1 = a[0] + a[1]
                b1 = b[0] + b[1]
            else:
                a1 = a[0]
                b1 = b[0]
            if int(a1) > int(b1):                  # Случай если отрицательное больше положительного
                s = ['']
                if len(a) == 2:
                    s.append('')
                    for i in range(len(a[1]) - 1, -1, -1):
                        if (a[1][i] == 'f') or int(a[1][i]) < int(b[1][i]):
                            if a[1][i] == 'f':
                                a[1] = a[1][:i] + '3' + a[1][(i + 1):]
                            else:
                                a[1] = a[1][:i] + str(int(a[1][i]) + 4) + a[1][(i + 1):]
                            if i == 0:
                                if str(int(a[0][len(a) - 1]) - 1) == '-1':
                                    a[0] = a[0][:(len(a[0]) - 1)] + 'f'
                                else:
                                    a[0] = a[0][:(len(a[0]) - 1)] + str(int(a[0][len(a) - 1]) - 1)
                            else:
                                if str(int(a[1][i - 1]) - 1) == '-1':
                                    a[1] = a[1][:(i - 1)] + 'f' + a[1][i:]
                                else:
                                    a[1] = a[1][:(i - 1)] + str(int(a[1][i - 1]) - 1) + a[1][i:]
                        print(a)
                        s[1] = str(int(a[1][i]) - int(b[1][i])) + s[1]
                for i in range(len(a[0]) - 1, -1, -1):
                    if (a[0][i] == 'f') or (int(a[0][i]) < int(b[0][i])):
                        if a[0][i] == 'f':
                            a[0] = a[0][:i] + '3' + a[0][(i + 1):]
                        else:
                            a[0] = a[0][:i] + str(int(a[0][i]) + 4) + a[0][(i + 1):]
                        if str(int(a[0][i - 1]) - 1) == '-1':
                            a[0] = a[0][:(i - 1)] + 'f' + a[0][i:]
                        else:
                            a[0] = a[0][:(i - 1)] + str(int(a[0][i - 1]) - 1) + a[0][i:]
                    print(a)
                    s[0] = str(int(a[0][i]) - int(b[0][i])) + s[0]
                print(a, '  ', b, ' result: ', s)
                print('-----------------------------------')
                s = s[0] + '.' + s[1]
                label2.config(text=s)
            else:                                       # Случай если положительное больше отрицательного при вычитании
                s = ['']
                if len(b) == 2:
                    s.append('')
                    for i in range(len(b[1]) - 1, -1, -1):
                        if (b[1][i] == 'f') or int(b[1][i]) < int(a[1][i]):
                            if b[1][i] == 'f':
                                b[1] = b[1][:i] + '3' + b[1][(i + 1):]
                            else:
                                b[1] = b[1][:i] + str(int(b[1][i]) + 4) + b[1][(i + 1):]
                            if i == 0:
                                if str(int(b[0][len(b) - 1]) - 1) == '-1':
                                    b[0] = b[0][:(len(b[0]) - 1)] + 'f'
                                else:
                                    b[0] = b[0][:(len(b[0]) - 1)] + str(int(b[0][len(b) - 1]) - 1)
                            else:
                                if str(int(b[1][i - 1]) - 1) == '-1':
                                    b[1] = b[1][:(i - 1)] + 'f' + b[1][i:]
                                else:
                                    b[1] = b[1][:(i - 1)] + str(int(b[1][i - 1]) - 1) + b[1][i:]
                        print(b)
                        s[1] = str(int(b[1][i]) - int(a[1][i])) + s[1]
                for i in range(len(b[0]) - 1, -1, -1):
                    if (b[0][i] == 'f') or (int(b[0][i]) < int(a[0][i])):
                        if b[0][i] == 'f':
                            b[0] = b[0][:i] + '3' + b[0][(i + 1):]
                        else:
                            b[0] = b[0][:i] + str(int(b[0][i]) + 4) + b[0][(i + 1):]
                        if str(int(b[0][i - 1]) - 1) == '-1':
                            b[0] = b[0][:(i - 1)] + 'f' + b[0][i:]
                        else:
                            b[0] = b[0][:(i - 1)] + str(int(b[0][i - 1]) - 1) + b[0][i:]
                    print(b)
                    s[0] = str(int(b[0][i]) - int(a[0][i])) + s[0]
                print(b, '  ', a, ' result: ', s)
                print('-----------------------------------')
                s = '-' + s[0] + '.' + s[1]
                label2.config(text=s)
    return 0


def schet(event):                           # Функция кнопки
    if check_digits() == 0:
        messagebox.showinfo("Error", "Введите данные правильно!")
    else:
        do_schet(digit1.get(), digit2.get())
        print('Ланг гет: ', lang.get())
    return 0


root = Tk()                         # Создание главного окна
root.title("Truntsev Calc")
root.geometry("350x250+1700+1000")

                                        # Создание меню
lang = IntVar()
lang.set(1)
zadan_menu = Menu(tearoff=0)
zadan_menu.add_radiobutton(label="Сложение", value=1, variable=lang)
zadan_menu.add_radiobutton(label="Вычитание", value=2, variable=lang)


chist_menu = Menu(tearoff=0)
chist_menu.add_command(label="Очистить только 1 число", command=chist1)
chist_menu.add_command(label="Очистить только 2 число", command=chist2)
chist_menu.add_command(label="Очистить только результат", command=chist3)
chist_menu.add_command(label="Все", command=chist4)


main_menu = Menu()
main_menu.add_cascade(label="Заданные действия", menu=zadan_menu)
main_menu.add_cascade(label="Очистка полей", menu=chist_menu)
main_menu.add_command(label="Инфо", command=info_click)


root.config(menu=main_menu)


digit1 = Entry()                # Создание полей ввода чисел
digit2 = Entry()

digit1.grid(row=0, column=1)
digit2.grid(row=1, column=1)

digit1_label = Label(text="Введите 1 число:")
digit2_label = Label(text="Введите 2 число:")

digit1_label.grid(row=0, column=0, sticky="w")
digit2_label.grid(row=1, column=0, sticky="w")


btn1 = Button(text="Посчитать")             # Создание кнопки и присвоение ей функций
btn1.grid(row=2, column=1)
btn1.bind("<Button-1>", schet)

label1 = Label(text="Результат:")
label1.grid(row=3, column=0)

label2 = Label(text="")
label2.grid(row=3, column=1)

btn2 = Button(text="0")
btn2.grid(row=0, column=3)
btn2.bind("<Button-1>", push1)

btn3 = Button(text="1")
btn3.grid(row=0, column=4)
btn3.bind("<Button-1>", push2)

btn4 = Button(text="2")
btn4.grid(row=0, column=5)
btn4.bind("<Button-1>", push3)

btn5 = Button(text="3")
btn5.grid(row=0, column=6)
btn5.bind("<Button-1>", push4)

btn6 = Button(text="0")
btn6.grid(row=1, column=3)
btn6.bind("<Button-1>", push5)

btn7 = Button(text="1")
btn7.grid(row=1, column=4)
btn7.bind("<Button-1>", push6)

btn8 = Button(text="2")
btn8.grid(row=1, column=5)
btn8.bind("<Button-1>", push7)

btn9 = Button(text="3")
btn9.grid(row=1, column=6)
btn9.bind("<Button-1>", push8)

btn10 = Button(text=".")
btn10.grid(row=0, column=7)
btn10.bind("<Button-1>", push9)

btn11 = Button(text=".")
btn11.grid(row=1, column=7)
btn11.bind("<Button-1>", push10)

btn11 = Button(text="-")
btn11.grid(row=0, column=2)
btn11.bind("<Button-1>", push11)

btn11 = Button(text="-")
btn11.grid(row=1, column=2)
btn11.bind("<Button-1>", push12)

root.mainloop()