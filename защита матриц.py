# Воякин Алексей Янович ИУ7-14б
# Защита матриц


# Ввод размера матрицы
n = int(input('Введите кол-во строк: '))
m = int(input('Введите кол-во столбцов: '))


# Задание матрицы
x = [0] * n
for i in range(n):
    x[i] = [0] * m

    
# Ввод данных в матрицу
for i in range(0, n):
    for j in range(0, m):
        print('Введите в строку: ', i + 1, ' столбец: ', j + 1)
        x[i][j] = int(input())


# Вывод начальной матрицы
for i in range(0, n):
    print()
    for j in range(0, m):
        print(x[i][j], ' ', end='')
print()


# Нахождение стобца с максимальным кол-вом нулей
kol = 0
ma = 0
ind = -1
for i in range(0, m):
    for j in range(0, n):
        if x[j][i] == 0:
            kol += 1
    if kol > ma:
        ma = kol
        ind = i
    kol = 0


# Объявление новой матрицы
if ind != -1:
    x1 = [0] * n
    for i in range(n):
        x1[i] = [0] * (m - 1)
if ind == -1:
    x1 = [0] * n
    for i in range(n):
        x1[i] = [0] * (m)
    x1 = x
# Заполнение новой матрицы
i1 = 0
if ind != -1:
    for i in range(0, m):
        for j in range(0, n):
            if i != ind:
                x1[j][i1] = x[j][i]
        if i != ind:
            i1 += 1

# Вывод матрицы с удалённым стобцом
if ind != -1:
    for i in range(0, n):
        print()
        for j in range(0, m - 1):
            print(x1[i][j], ' ', end='')
print()


# Объявление новой матрицы
if ind != -1:
    x = [0] * (n + 1)
    for i in range(n + 1):
        x[i] = [0] * (m - 1)
if ind == -1:
    x = [0] * (n + 1)
    for i in range(n + 1):
        x[i] = [0] * (m)

# Заполнение новой матрицы
if ind != -1:
    for i in range(0,m-1):
        for j in range(0, n+1):
            if j < n // 2 + 1:
                x[j][i] = x1[j][i]
            elif j == n // 2 + 1:
                x[j][i] = x1[j-1][i-1] * 2
            else:
                x[j][i] = x1[j-1][i-1]

if ind == -1:
    for i in range(0,m):
        for j in range(0, n+1):
            if j < n // 2 + 1:
                x[j][i] = x1[j][i]
            elif j == n // 2 + 1:
                x[j][i] = x1[j-1][i-1] * 2
            else:
                x[j][i] = x1[j-1][i-1]

if ind != -1:
    for i in range(0, n + 1):
        print()
        for j in range(0, m - 1):
            print(x[i][j], ' ', end='')
if ind == -1:
    for i in range(0, n + 1):
        print()
        for j in range(0, m):
            print(x[i][j], ' ', end='')
print()

