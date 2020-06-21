# Воякин Алексей Янович
# Текст с меню


def top(h):
    return h[len(h) - 1]


postsort = 0
# Ввод данных
s = ['Зима  была  4 + 5 * 6   суровая.  6 / 3 + 2 Белый      ',
     'иней                 был на      машинах. Везде ',
     '          был снег. Всё ',
     '( 4 - ( 5 - 1 ) )',
     'казалось   хрустальным.     И я не мог ( 5 + 4 ) / 3 / 0',
     '            выйти на улицу.']


# Вывод исходных строк
for i in range(len(s)):
    print(s[i])


# Удаление пустых строк
kol = len(s)
i = 0
while i < kol:
    if s[i] == '':
        del(s[i])
        kol -= 1
    else:
        i += 1

# Удаление пробалов в начале и в конце
kol = len(s)
ok = True
while ok:
    ok = False
    for i in range(kol):
        rab = s[i]
        while rab[0] == ' ' or rab[len(rab)-1] == ' ':
            if rab[0] == ' ':
                rab = rab[1:]
            if rab[len(rab)-1] == ' ':
                rab = rab[:len(rab)-1]
        s[i] = rab

# Удаление лишних пробелов между словами
for i in range(len(s)):
    rab = s[i].split(' ')
    kol = len(rab)
    j = 0
    while rab.count('') != 0 and j < len(rab):
        if rab[j] == ' ' or rab[j] == '':
            del rab[j]
            kol -= 1
        else:
            j += 1
    rab = ' '.join(rab)
    s[i] = rab


menu = 1
while menu != 8:

    # Вывод вариантов меню на экран
    print()
    print('(1) Выравнивание по ширине')
    print('(2) Выравнивание по левому краю')
    print('(3) Выравнивание по правому краю')
    print('(4) Замена во всем тексте одного слова другим')
    print('(5) Удаление заданного слова из текста')
    print('(6) Замена арифм. выражений на результат их вычисления')
    print('(7) Найти предложение в котором есть слово с максимальным числом гласных букв')
    print('(8) Закончить выполнение программы')
    print()

    # Выбор пункта меню
    ok = False
    while not ok:
        ok = True
        menu = input('Выберете нужное преобразование: ')
        try:
            menu = int(menu)
            if menu < 1 or menu > 8:
                print('Неверный ввод, повторите попытку...')
                ok = False
        except:
            print('Неверный ввод, повторите попытку...')
    print()

    # (1) пункт
    if menu == 1:
        postsort = 1
        kol = len(s)
        ok = True
        while ok:
            ok = False
            for i in range(kol):
                rab = s[i]
                while rab[0] == ' ' or rab[len(rab)-1] == ' ':
                    if rab[0] == ' ':
                        rab = rab[1:]
                    if rab[len(rab)-1] == ' ':
                        rab = rab[:len(rab)-1]
                s[i] = rab
        ma = len(s[1])
        for i in range(len(s)):
            if len(s[i]) > ma:
                ma = len(s[i])
                
        rab = [0]*len(s)
        for i in range(len(s)):
            rab[i] = s[i]

        for i in range(len(rab)):
            buff = rab[i].split(' ')
            if len(buff) == 1:
                rab[i] = buff
            else:
                kol = ma - len(rab[i])
                k = 0
                while kol != k:
                    for j in range(len(buff)-1):
                        if k != kol:
                            buff[j] += ' '
                            rab[i] = buff
                            k += 1
            rab[i] = buff
            s[i] = rab[i]
            print(*s[i])
            s[i] = ' '.join(s[i])

    # (2) пункт
    if menu == 2:
        postsort = 2
        for i in range(len(s)):
            rab = s[i].split(' ')
            kol = len(rab)
            j = 0
            while rab.count('') != 0 and j < len(rab):
                if rab[j] == ' ' or rab[j] == '':
                    del rab[j]
                    kol -= 1
                else:
                    j += 1
            rab = ' '.join(rab)
            s[i] = rab

        ma = len(s[1])
        for i in range(len(s)):
            if len(s[i]) > ma:
                ma = len(s[i])
        for i in range(len(s)):
            print(s[i], ' ' * (ma - len(s[i])), sep='')

    # (3) пункт
    if menu == 3:
        postsort = 3
        ma = len(s[1])
        for i in range(len(s)):
            if len(s[i]) > ma:
                ma = len(s[i])
        for i in range(len(s)):
            s[i] = ' ' * (ma - len(s[i])) + s[i]
            print(s[i])

    # (4) пункт
    if menu == 4:
        word1 = str(input('Введите слово, которое нужно заменить: ')).lower()
        word2 = str(input('Введите слово, на которое нужно нужно заметить: '))
        print()
        ok1 = False
        for i in range(len(s)):
            rab = s[i].split(' ')
            for j in range(len(rab)):
                x = str(rab[j].lower())
                if x == word1:
                    rab[j] = word2
                    ok1 = True
                elif x.replace(',', '') == word1:
                    rab[j] = word2
                    rab[j] += ','
                    ok1 = True
                elif x.replace('.', '') == word1:
                    rab[j] = word2
                    rab[j] += '.'
                    ok1 = True
            s[i] = rab
            print(*s[i], sep=' ')
            s[i] = ' '.join(s[i])
        if not ok1:
            print('Слово не найдено')

    # (5) пункт
    if menu == 5:
        word1 = str(input('Введите слово, нужное удалить: ')).lower()
        print()
        ok2 = False
        for i in range(len(s)):
            rab = s[i].split(' ')
            j = 0
            kol = len(rab)
            while j < kol:
                x = str(rab[j].lower())
                if x == word1:
                    del(rab[j])
                    ok2 = True
                    kol -= 1
                elif x.replace(',', '') == word1:
                    del(rab[j])
                    ok2 = True
                    if i != 0:
                        rab[j - 1] += ','
                    kol -= 1
                elif x.replace('.', '') == word1:
                    del(rab[j])
                    ok2 = True
                    if i != 0:
                        rab[j - 1] += '.'
                    kol -= 1
                j += 1
            s[i] = rab
            print(*s[i], sep=' ')
            s[i] = ' '.join(s[i])
        if not ok2:
            print('Слово не найдено')


    # (6) пункт
    if menu == 6:
        for i in range(len(s)):
            rab = s[i].split(' ')
            kol = len(rab)
            j = 0
            while rab.count('') != 0 and j < len(rab):
                    if rab[j] == ' ' or rab[j] == '':
                        del rab[j]
                        kol -= 1
                    else:
                        j += 1
            ari = []
            for j in range(len(rab)):
                if rab[j].isdigit() or rab[j] in '+-*/()':
                    ari.append(rab[j])
                    rab[j] = ' '
                    if j == len(rab) - 1:
                        a = []
                        b = []
                        d = 0
                        ok3 = True
                        while d != len(ari):
                            if ari[d] in '()*/-+':
                                if not b:
                                    b.append(ari[d])
                                    d += 1
                                elif ari[d] == '(':
                                    b.append(ari[d])
                                    d += 1
                                elif ari[d] in '+-*/' and top(b) in '(':
                                    b.append(ari[d])
                                    d += 1
                                elif ari[d] in '/*' and top(b) in '-+':
                                    b.append(ari[d])
                                    d += 1
                                elif ari[d] in '/*' and top(b) in '/*':
                                    if len(a) < 2:
                                        print('Выражение построено неверно')
                                        ok3 = False
                                        break
                                    g1 = a.pop()
                                    g2 = a.pop()
                                    if top(b) == '*':
                                        a.append(g2 * g1)
                                        trash = b.pop()
                                    elif top(b) == '/':
                                        if g1 == 0:
                                            a = []
                                            a.append('Nan')
                                            b = []
                                        else:
                                            a.append(g2 / g1)
                                            trash = b.pop()
                                elif ari[d] in '+-' and top(b) in '-+':
                                    if len(a) < 2:
                                        print('Выражение построено неверно')
                                        ok3 = False
                                        break
                                    g1 = a.pop()
                                    g2 = a.pop()
                                    if top(b) == '+':
                                        a.append(g2 + g1)
                                        trash = b.pop()
                                    elif top(b) == '-':
                                        a.append(g2 - g1)
                                        trash = b.pop()
                                elif ari[d] in '+-' and top(b) in '*/':
                                    if len(a) < 2:
                                        print('Выражение построено неверно')
                                        ok3 = False
                                        break
                                    g1 = a.pop()
                                    g2 = a.pop()
                                    if top(b) == '*':
                                        a.append(g2 * g1)
                                        trash = b.pop()
                                    elif top(b) == '/':
                                        if g1 == 0:
                                            a = []
                                            a.append('Nan')
                                            b = []
                                        else:
                                            a.append(g2 / g1)
                                            trash = b.pop()
                                elif ari[d] == ')' and top(b) != '(':
                                    if len(a) < 2:
                                        print('Выражение построено неверно')
                                        ok3 = False
                                        break
                                    g1 = a.pop()
                                    g2 = a.pop()
                                    if top(b) == '+':
                                        a.append(g2 + g1)
                                        trash = b.pop()
                                    elif top(b) == '-':
                                        a.append(g2 - g1)
                                        trash = b.pop()
                                    elif top(b) == '*':
                                        a.append(g2 * g1)
                                        trash = b.pop()
                                    elif top(b) == '/':
                                        if g1 == 0:
                                            a = []
                                            a.append('Nan')
                                            b = []
                                        else:
                                            a.append(g1 / g2)
                                            trash = b.pop()
                                elif ari[d] == ')' and top(b) == '(':
                                    trash = b.pop()
                                    d += 1
                            else:
                                try:
                                    ari[d] = float(ari[d])
                                except:
                                    print('Выражение построено неверно')
                                    ok3 = False
                                    break
                                a.append(ari[d])
                                d += 1
                        while not (not b) and ok3:
                            if top(b) in '+-*/':
                                if len(a) < 2:
                                    print('Выражение построено неверно')
                                    ok3 = False
                                    break
                                g1 = a.pop()
                                g2 = a.pop()
                                if top(b) == '+':
                                    a.append(g2 + g1)
                                    trash = b.pop()
                                elif top(b) == '-':
                                    a.append(g2 - g1)
                                    trash = b.pop()
                                elif top(b) == '*':
                                    a.append(g2 * g1)
                                    trash = b.pop()
                                elif top(b) == '/':
                                    if g1 == 0:
                                        a = []
                                        a.append('Nan')
                                        b = []
                                    else:
                                        a.append(g1 / g2)
                                        trash = b.pop()
                            elif top(b) == '(':
                                print('Выражение построено неверно')
                                ok3 = False
                                break
                        if a[0] == 'Nan':
                            rab[j] = str(a[0])
                        else:
                            rab[j] = str(int(a[0]))
                        ari = []
                else:
                    if not(not ari):
                        a = []
                        b = []
                        d = 0
                        ok3 = True
                        while d != len(ari):
                            if ari[d] in '()*/-+':
                                if not b:
                                    b.append(ari[d])
                                    d += 1
                                elif ari[d] == '(':
                                    b.append(aro[d])
                                    d += 1
                                elif ari[d] in '+-*/' and top(b) in '(':
                                    b.append(ari[d])
                                    d += 1
                                elif ari[d] in '/*' and top(b) in '-+':
                                    b.append(ari[d])
                                    d += 1
                                elif ari[d] in '/*' and top(b) in '/*':
                                    if len(a) < 2:
                                        print('Выражение построено неверно')
                                        ok3 = False
                                        break
                                    g1 = a.pop()
                                    g2 = a.pop()
                                    if top(b) == '*':
                                        a.append(g2 * g1)
                                        trash = b.pop()
                                    elif top(b) == '/':
                                        if g1 == 0:
                                            a = []
                                            a.append('Nan')
                                            b = []
                                        else:
                                            a.append(g1 / g2)
                                            trash = b.pop()
                                elif ari[d] in '+-' and top(b) in '-+':
                                    if len(a) < 2:
                                        print('Выражение построено неверно')
                                        ok3 = False
                                        break
                                    g1 = a.pop()
                                    g2 = a.pop()
                                    if top(b) == '+':
                                        a.append(g2 + g1)
                                        trash = b.pop()
                                    elif top(b) == '-':
                                        a.append(g2 - g1)
                                        trash = b.pop()
                                elif ari[d] in '+-' and top(b) in '*/':
                                    if len(a) < 2:
                                        print('Выражение построено неверно')
                                        ok3 = False
                                        break
                                    g1 = a.pop()
                                    g2 = a.pop()
                                    if top(b) == '*':
                                        a.append(g2 * g1)
                                        trash = b.pop()
                                    elif top(b) == '/':
                                        if g1 == 0:
                                            a = []
                                            a.append('Nan')
                                            b = []
                                        else:
                                            a.append(g1 / g2)
                                            trash = b.pop()
                                elif ari[d] == ')' and top(b) != '(':
                                    if len(a) < 2:
                                        print('Выражение построено неверно')
                                        ok3 = False
                                        break
                                    g1 = a.pop()
                                    g2 = a.pop()
                                    if top(b) == '+':
                                        a.append(g2 + g1)
                                        trash = b.pop()
                                    elif top(b) == '-':
                                        a.append(g2 - g1)
                                        trash = b.pop()
                                    elif top(b) == '*':
                                        a.append(g2 * g1)
                                        trash = b.pop()
                                    elif top(b) == '/':
                                        if g1 == 0:
                                            a = []
                                            a.append('Nan')
                                            b = []
                                        else:
                                            a.append(g1 / g2)
                                            trash = b.pop()
                                elif ari[d] == ')' and top(b) == '(':
                                    trash = b.pop()
                                    d += 1
                            else:
                                try:
                                    ari[d] = float(ari[d])
                                except:
                                    print('Выражение построено неверно')
                                    ok3 = False
                                    break
                                a.append(ari[d])
                                d += 1
                        while not (not b) and ok3:
                            if top(b) in '+-*/':
                                if len(a) < 2:
                                    print('Выражение построено неверно')
                                    ok3 = False
                                    break
                                g1 = a.pop()
                                g2 = a.pop()
                                if top(b) == '+':
                                    a.append(g2 + g1)
                                    trash = b.pop()
                                elif top(b) == '-':
                                    a.append(g2 - g1)
                                    trash = b.pop()
                                elif top(b) == '*':
                                    a.append(g2 * g1)
                                    trash = b.pop()
                                elif top(b) == '/':
                                    if g1 == 0:
                                        a = []
                                        a.append('Nan')
                                        b = []
                                    else:
                                        a.append(g1 / g2)
                                        trash = b.pop()
                            elif top(b) == '(':
                                print('Выражение построено неверно')
                                ok3 = False
                                break
                        if a[0] == 'Nan':
                            rab[j-1] = str(a[0])
                        else:
                            rab[j-1] = str(int(a[0]))
                        ari = []
            d = 0
            kol = len(rab)
            while d < kol:
                if rab[d] == ' ':
                    del(rab[d])
                    kol -= 1
                else:
                    d += 1
            s[i] = rab
            s[i] = ' '.join(s[i])
        if postsort == 1:
            ma = len(s[1])
            for i in range(len(s)):
                if len(s[i]) > ma:
                    ma = len(s[i])
                
            rab = [0]*len(s)
            for i in range(len(s)):
                rab[i] = s[i]

            for i in range(len(rab)):
                buff = rab[i].split(' ')
                if len(buff) == 1:
                    rab[i] = buff
                else:
                    kol = ma - len(rab[i])
                    k = 0
                    while kol != k:
                        for j in range(len(buff)-1):
                            if k != kol:
                                buff[j] += ' '
                                rab[i] = buff
                                k += 1
                rab[i] = buff
                s[i] = rab[i]
                print(*s[i])
                s[i] = ' '.join(s[i])
        elif postsort == 0 or postsort == 2:
            for i in range(len(s)):
                print(s[i])
        elif postsort == 3:
            ma = len(s[1])
            for i in range(len(s)):
                if len(s[i]) > ma:
                    ma = len(s[i])
            for i in range(len(s)):
                s[i] = ' ' * (ma - len(s[i])) + s[i]
                print(s[i])

    # (7) пункт
    if menu == 7:
        mglas = 0
        z = []
        for i in range(len(s)):
            rab = s[i].split(' ')
            for j in range(len(rab)):
                z.append(rab[j])
        for i in range(len(z)):
            x = str(z[i].lower())
            kol = 0
            for k in range(len(x)):
                if x[k] in 'аеёиоуыэюя':
                    kol += 1
            if kol > mglas:
                mglas = kol
        k = 0
        k1 = -1
        for i in range(len(z)):
            x = str(z[i].lower())
            kol = 0
            for j in range(len(x)):
                if x[j] in 'аеёиоуыэюя':
                    kol += 1
            if kol == mglas:
                for o in range(i, len(z)):
                    p = z[o]
                    for l in range(len(p)):
                        if p[l] in '.':
                            k1 = o
                            break
                    if k1 == o:
                        break
                for o in range(k, k1 + 1):
                    print(z[o], end=' ')
                print()
            u = z[i]
            for y in range(len(u)):
                if u[y] in '.':
                    k = i + 1
