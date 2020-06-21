# Воякин Алексей Янович Иу7-14б
# Одномерный массив


# Ввод длины массива с проверкой на целые числа
ok = False
while not(ok):
    ok = True
    kole = 0
    kolm = 0
    kolt = 0
    mese = -1
    mesm = -1
    mes = -1
    oshi = (input('Введите длину массива: '))
    if oshi.isdigit():
        oshi = int(oshi)
        if oshi < 1 :
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
            if oshi < 1:
                ok = False
        if ok and kolm == 1 and kole == 0:
            ok = False
        if ok == False:
            print('Данные введены неверно, повторите ввод...')
lon = int(oshi)


# Объявление массива и переменных
s = []
su = 0
pr = 1
ok = False



# Заполнение массива элементами с проверкой вводимых элементов
for i in range(0, lon, 1):
    while not(ok):
        print('Введите',i + 1, 'элемент: ')
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
    su += x
    pr *= x
    s.append(x)
    ok = False
pr = abs(pr)


# Выполнение программы
srar = su / lon
srge = pr ** (1 / lon)


# Вывод данных
print('Среднее арифметическое равно = ', '{:.5g}'.format(srar))
print('Среднее геометрическое равно = ', '{:.5g}'.format(srge))
if srar > srge:
    print('Среднее арифметическое больше')
elif srar < srge:
    print('Среднее геометрическое больше')
else:
    print('Равны')
