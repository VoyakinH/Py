# Воякин Алексей Янович ИУ7-14б
# Удалить строки с лиш символами и отсортировать


# Ввод матрицы и её размера
n,m = map(int,input('Введите размер матрицы: ').split(' '))
r = [0] * n
rab = [0] * m
for i in range(0,n):
    ok = False
    while not(ok):
        ok = True
        print('Введите', i + 1, 'строку: ')
        s = str(input())
        koe = 0
        buf = ''
        for j in range(0, len(s)):
            if koe == m:
                ok = False
                break
            if s[j] != ' ':
                buf += s[j]
            if s[j] == ' ' or j == len(s) - 1:
                rab[koe] = buf
                buf = ''
                koe += 1
        if koe < m:
            ok = False
        if not(ok):
            print('Не соблюдён размер массива')
    r[i] = [0] * m
    for j in range(0, m):
        r[i][j] = rab[j]


# Вывод начальной матрицы
print()
print('Вывод исходной матрицы:')
for i in range(0,n):
    for j in range(0,m):
        if j != m - 1:
            print(r[i][j], end = ' ')
        else:
            print(r[i][j])


# Обработка матрицы
lish = 0
for i in range(n - 1, -1, -1):
    ok = True
    for j in range(m):
        if not r[i][j].isalpha():
            ok = False
    if not ok:
        for j in range(m):
            for o in range(i, n - 1 - lish):
                r[o][j] = r[o + 1][j]
        lish += 1
print()        


# Вывод матрицы до сортировки
print('Матрица с удалёнными строками до сортировки:')
for i in range(0,n - lish):
    for j in range(0,m):
        if j != m - 1:
            print(r[i][j], end = ' ')
        else:
            print(r[i][j])


# Сортировка полученной матрицы
for i in range(n - 1 - lish):
    for j in range(i + 1, n - lish):
        if r[i][0] > r[j][0]:
            for o in range(m):
                r[i][o],r[j][o] = r[j][o],r[i][o]


# Вывод отсортированной матрицы
print()
print('Матрица с удалёнными строками после сортировки:')
for i in range(0,n - lish):
    for j in range(0,m):
        if j != m - 1:
            print(r[i][j], end = ' ')
        else:
            print(r[i][j])
