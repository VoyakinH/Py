# Воякин Алексей Янович ИУ7-14б
# Удалить слова с большой буквы


fin = False
while not fin:         # Цикл для возможности многократного ввода
    lish = 0
    z1 = str(input('Введите строку: '))             # Ввод строки
    z = [' '] * len(z1)
    for i in range(len(z1)):                        # Занос строки с список
        z[i] = z1[i]
    for i in range(len(z) - 1, -1, -1):             # Обход списка с конца
        if i == len(z) - 1 and z[i] == ' ':
            lish += 1
        if i != len(z) - 1:
            if z[i] == ' ' and (z[i + 1] == ' ' or i == 0):     # Удаление лишних пробелов
                lish += 1
                for j in range(i, len(z) - 1):
                    z[j] = z[j + 1]
            if z[i].isupper() and (z[i - 1] == ' ' or i == 0):  # Удаление слов с большой буквы
                kol = 0
                for j in range(i, len(z)):        # Вычисление длины слова
                    if z[j] != ' ':
                        kol += 1
                    else:
                        break
                for j in range(0, kol):           # Смещение до полного удаление слова
                    lish += 1
                    for o in range(i, len(z) - 1):
                        z[o] = z[o + 1]
    for i in range(0, len(z) - lish):             # Дополнительный обход с начала для удаления пробелов
        if i == 0 and z[i] == ' ':
            for j in range(0, len(z) - 1 - lish):
                z[j] = z[j + 1]
            lish += 1
        if i == len(z) - 1 - lish and z[len(z) - 1 - lish] == ' ':
            lish += 1
    for i in range(0, len(z) - lish):             # Вывод полученной строки
        print(z[i], end='')
    print()
    print('Длина строки =', len(z) - lish)        # Вывод длины строки
    f = str(input('Продолжить ввод(Д/Н): '))
    if f == 'Н':
        fin = True
