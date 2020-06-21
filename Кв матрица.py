# Воякин Алексей Янович ИУ7-14б
# Разворот квадратной матрицы


# Ввод размера матрицы с проверкой
ok = False
oshi = 0
while not ok:
    ok = True
    kole = 0
    kolm = 0
    kolt = 0
    mese = -1
    mesm = -1
    mes = -1
    oshi = (input('Введите размер матрицы: '))
    if oshi.isdigit():
        oshi = int(oshi)
        if oshi > 7 or oshi < 2:
            ok = False
            print('Данные введены неверно, повторите ввод...')
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
        if ok and kolm > 1:
            ok = False
        if ok and oshi == 'e':
            ok = False
        if ok and mesm == 0:
            ok = False
        if ok and mese == len(oshi) - 1:
            ok = False
        if ok and mesm != mese + 1 and kolm == 1 and kole == 1:
            ok = False
        if ok and kole > 1:
            ok = False
        if ok and mese == 0:
            ok = False
        if ok and kolt > 1:
            ok = False
        if ok and mes > mese and kole == 1:
            ok = False
        if ok and kole != 1 and kolt > 0:
            ok = False
        if ok and kole == 1:
            oshi = int(float(oshi))
            if oshi > 7 or oshi < 2:
                ok = False
        if ok and kolm == 1 and kole == 0:
            ok = False
        if not ok:
            print('Данные введены неверно, повторите ввод...')
h = int(oshi)
ok = False


# Задание матрицы
x = [0] * h
for i in range(h):
    x[i] = [0] * h


# Ввод данных в матрицу с проверкой
for i1 in range(0, h):
    for j1 in range(0, h):
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
                if ok and kolm == 1 and len(oshi) == 1:
                    ok = False
                if ok and mese == 0:
                    ok = False
                if ok and kolt > 1:
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
        x[i1][j1] = int(oshi)


# Вывод начальной матрицы
for i in range(0, h):
    print()
    for j in range(0, h):
        print(x[i][j], ' ', end='')
print()


# Разворот матрицы на 180
for i in range(0, h // 2 + 1):
    if i == h // 2:
        for j in range(0, h // 2):
            x[i][j], x[h - (i + 1)][h - (j + 1)] = x[h - (i + 1)][h - (j + 1)], x[i][j]
    else:
        for j in range(0, h):
            x[i][j], x[h - (i + 1)][h - (j + 1)] = x[h - (i + 1)][h - (j + 1)], x[i][j]


# Вывод полученной матрицы
for i in range(0, h):
    print()
    for j in range(0, h):
        print(x[i][j], ' ', end='')