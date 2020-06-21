# Воякин Алексей Янович ИУ7-14б
# Координаты точек в массиве


from math import sqrt


# Определение переменных
s = []
bol = 0
oshi = 'g'
maxras = 0
max1 = 0
max2 = 0
x = 'g'
y = 'g'
yi = 1
xi = 1


# Ввод кол-ва точек с проверкой
ok = False
while not(ok):
    ok = True
    kole = 0
    kolm = 0
    kolt = 0
    mese = -1
    mesm = -1
    mes = -1
    oshi = (input('Введите кол-во точек: '))
    if oshi.isdigit():
        oshi = int(oshi)
        if oshi < 2 :
            ok = False
            print('Данные введены неверно, повторите ввод...')
    else:
        for i in range (0, len(oshi)):
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
            if oshi < 2:
                ok = False
        if ok and kolm == 1 and kole == 0:
            ok = False
        if ok == False:
            print('Данные введены неверно, повторите ввод...')
n = int(oshi)
ok = False


# Ввод координат с проверкой
for i in range(1, (n * 2) + 1):
    if i % 2 == 0:
        print('Введите координату y ', yi, '-ой точки: ', sep='')
        yi += 1
    else:
        print('Введите координату x ', xi, '-ой точки: ', sep='')
        xi += 1
    while not(ok):
        x = input()
        ok = True
        kole = 0
        kolm = 0
        kold = 0
        kolt = 0
        mese = -1
        mesm = -1
        mes = -1
        for j in range (0, len(x)):
            if x[j] in {'-', 'e', '.'} or x[j].isdigit():
                fuck = 0
                if x[j] == 'e':
                    kole += 1
                    mese = j
                if x[j] == '-':
                    kolm += 1
                    mesm = j
                if x[j] == '.':
                    kolt += 1
                    mes = j
            else:
                ok = False
        if ok and kolm > 1 and kole != 1:
            ok = False
        if ok and kolt > 1:
            ok = False
        if ok and mes > mese and mese == 1:
            ok = False
        if ok and kole == 1 and kolm > 2:
            ok = False
        if ok and kole == 0 and kolt > 1:
            ok = False
        if ok and kole == 0 and kolm == 1 and kolt == 1 and (j == 2 or j == len(x)):
            ok = False
        if ok and kolm == 1 and (mesm != 0 or len(x) == 1) and kole != 1:
            ok = False
        if ok and kolm == 1 and kole == 1 and (mese == 1 or mese == len(x)):
            ok = False
        if ok and kolm != 1 and kole == 1 and (mese == 0 or mese == len(x)):
            ok = False
        if ok and kole > 1:
            ok = False
        if ok and kolm == 2 and kole == 1 and (x[0] != '-' or x[mesm - 1] != 'e'):
            ok = False
        if ok and mes > mese and kole == 1 and kolt >= 1:
            ok = False
        if ok and x == '' or x == '.':
            ok = False
        if ok and mese == 0:
            ok = False
        if ok and mese == len(x) - 1:
            ok = False
        if ok and kolm == 1 and mesm != 0 and mesm != mese + 1:
            ok = False
        if ok and kolm == 2 and (x[0] != '-' or x[mese + 1] != '-'):
            ok = False
        if ok and len(x) != 1 and not(x[mesm + 1].isdigit()):
            ok = False
        if not(ok):
            print('Данные введены неверно, повторите ввод')
        if ok and kole <= 1:
            x = float(x)
    s.append(x)
    ok = False



# Нахождение расстояния между точками
for i in range(1, n * 2 - 2, 2):
    for j in range(i + 2, n * 2, 2):
        ras = sqrt((s[i - 1] - s[j - 1]) ** 2 + ((s[i] - s[j]) ** 2))
        if bol == 0:
            maxras = ras
            max1 = i
            max2 = j
            bol += 1
        if ras > maxras:
            maxras = ras
            max1 = i
            max2 = j
print('Координаты первой точки: ', 'x=', s[max1 - 1], ' ', 'y=', s[max1], sep='')
print('Координаты второй точки: ', 'x=', s[max2 - 1], ' ', 'y=', s[max2], sep='')
print('Расстояние между данными точками =', '{:.5g}'.format(maxras))
