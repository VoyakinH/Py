# Воякин Алексей Янович ИУ7-14б


# Ввод данных
n, m = map(int, input('Введите размер матрицы: ').split(' '))
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
for i in range(0,n):
    for j in range(0,m):
        if j != m - 1:
            print(r[i][j], end = ' ')
        else:
            print(r[i][j])



# Обработка матрицы
for i in range(n):
    for j in range(m):
        g1 = 0
        g2 = 0
        el = r[i][j]
        while g1 < n and el.isdigit():
            if not(r[g1][j].isdigit()):
                r[g1][j] = '#'
            g1 += 1
        while g2 < m and el.isdigit():
            if not(r[i][g2].isdigit()):
                r[i][g2] = '#'
            g2 += 1
print()
for i in range(n):
    for j in range(m):
        if r[i][j].isdigit():
            r[i][j] = '#'



# Вывод полученной матрицы
for i in range(0,n):
    for j in range(0,m):
        if j != m - 1:
            print(r[i][j], end = ' ')
        else:
            print(r[i][j])   
