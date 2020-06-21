n = int(input('Введите кол-во строк: '))
m = int(input('Введите кол-во столбцов: '))

x = [0] * n
for i in range(0,n):
    x[i] = [0] * m
    
for i in range(0, n):
    for j in range(0, m):
        print('Введите в строку: ', i + 1, ' столбец: ', j + 1)
        x[i][j] = int(input())

for i in range(0, n):
    print()
    for j in range(0, m):
        print(x[i][j], ' ', end='')
print()

kol = 0
for i in range(m-1, -1,-1):
    if x[0][i] == 0:
        ok = True
        for j in range(0, n):
            if x[j][i] != 0:
                ok = False
        if ok:
            kol += 1
            for i1 in range(0,n):
                for j1 in range(i,m-1):
                    x[i1][j1] = x[i1][j1+1]

for i in range(0, n):
    print()
    for j in range(0, m-kol):
        print(x[i][j], ' ', end='')
print()
