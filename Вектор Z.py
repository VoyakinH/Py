# Воякин Алексей Янович ИУ7-14б
# Cформировать вектор Z


# Объявление размеров матрицы B
h1 = 4
h2 = 4


# Задание матрицы
x = [0] * h1
for i in range(h1):
    x[i] = [0] * h2


# Ввод данных в матрицу с проверкой
s = []
ok = False
for i1 in range(0, h1):
    for j1 in range(0, h2):
        print('Введите в строку: ', i1 + 1, ' столбец: ', j1 + 1)
        oshi = 0
        while not ok:
            ok = True
            kole = 0
            kolm = 0
            kolt = 0
            mese = -1
            mesm = -1
            mes = -1
            oshi = (input())
            if oshi.isdigit():
                oshi = int(oshi)
            else:
                for i in range(0, len(oshi)):
                    if oshi[i] in {'-', 'e', '.'} or oshi[i].isdigit():
                        fuck = 0
                        if oshi[i] == 'e':
                            kole += 1
                            mese = i
                        if oshi[i] == '-':
                            kolm += 1
                            mesm = i
                        if oshi[i] == '.':
                            kolt += 1
                            mes = i
                    else:
                        ok = False
                if ok and kolm > 2 and kole == 1:
                    ok = False
                if kolm > 1 and kole == 0:
                    ok = False
                if ok and oshi == 'e':
                    ok = False
                if ok and mese == len(oshi) - 1:
                    ok = False
                if ok and kolm == 2 and (oshi[0] != '-' or oshi[mese + 1] != '-') and kole == 1:
                    ok = False
                if ok and kolm == 1 and kole == 1 and oshi[0] != '-' and oshi[mese + 1] != '-':
                    ok = False
                if kolm == 1 and kole == 0 and oshi[0] != '-':
                    ok = False
                if ok and kole > 1:
                    ok = False
                if ok and mese == 0:
                    ok = False
                if ok and kolt > 1:
                    ok = False
                if ok and kolm == 1 and len(oshi) == 1:
                    ok = False
                if ok and mes > mese and kole == 1:
                    ok = False
                if ok and kole != 1 and kolt > 0:
                    ok = False
                if ok and kole == 1:
                    oshi = int(float(oshi))
                if not ok:
                    print('Данные введены неверно, повторите ввод...')
        ok = False
        oshi = int(oshi)
        x[i1][j1] = oshi
        if oshi != 0:
            s.append(oshi)


# Вывод начальной матрицы
for i in range(0, h1):
    print()
    for j in range(0, h2):
        print(x[i][j], ' ', end='')
print()


# Замена третьего элемента
kol = 0
pr = 1
for i in range(0, len(s)):
    if s[i] > 0:
        kol += 1
        if kol < 3:
            pr *= s[i]
        if kol == 3:
            s[i] = pr
if kol < 3:
    print('Кол-во положительных элементов меньше трёх')
if len(s) == 0:
    print('Кол-во положительных элементов меньше трёх')
if len(s) != 0:
    print(s)
