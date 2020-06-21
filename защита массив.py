# Воякин Алексей Янович ИУ7-14б
# Защита массивов


# Ввод данных
h = int(input('Введите длину массива: '))
s1 = []
s2 = []
summ = 0
kol = 0
for i in range(0, h):
    print('Введите',i + 1,'элемент: ')
    x = float(input())
    summ += x
    s1.append(x)
print(s1)


# Обработка данных
srar = summ / h
for i in range(0, h):
    if s1[i] > srar and (i + 1) % 2 == 0:
        kol += 1
        for j in range(i,h - 1):
            s1[j] = s1[j + 1]
print(srar)
for i in range(0,h - kol):
    s2.append(s1[i])
print(s2)
