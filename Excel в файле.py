
# Набор записей одинаковой структуры в файле
# Воякин Алексей Янович ИУ7-14б





menu = 8
name = 'empty'
while menu != 7:

    print()
    print('(1) Выбор файла')
    print('(2) Создание нового набора записей')
    print('(3) Добавление записи')
    print('(4) Вывод всех записей')
    print('(5) Поиск по одному полю')
    print('(6) Поиск по двум полям')
    print('(7) Закончить выполнение программы')
    print()

    # Выбор действия с проверкой 
    ok = False
    while not ok:
        ok = True
        menu = str(input('Введите номер необходимого действия: '))
        try:
            menu = int(menu)
            if menu > 7 or menu < 1:
                ok = False
            if name == 'empty' and menu > 1 and menu < 7:
                ok = False
                print('Выполните выбор файла')
        except: ok = False

    # (1) пункт
    if menu == 1:
        ok = False
        while not ok:
            ok = True
            name = str(input('Введите имя файла: '))
            try:
                f = open(name, 'r')
                f.close()
            except:
                ok = False
                print('Файл не найден')
        print()
        print('Файл найден!')

    # (2) пункт
    if menu == 2:
        alert = str(input('Содержимое файла будет удалено. Продолжить? (да/нет): '))
        if alert.lower() == 'да':
            f = open(name, 'w')
            print('# - конец ввода')
            print()
            txt = str(input())
            l = txt.split(' ')
            l = len(l)
            while txt != '#':
                st = txt.split(' ')
                if l == len(st):
                    for index in txt:
                        f.write(index)
                    f.write('\n')
                else:
                    print('Структура различается, повторите ввод...')
                txt = str(input())
            print()
            print('Набор записей сохранён в файл.')
            f.close()
                
    # (3) пункт
    if menu == 3:
        f = open(name, 'r')
        l = f.readline()
        l = l.split(' ')
        l = len(l)
        f.close()
        f = open(name, 'a')
        ok = False
        while not ok:
            ok = True
            txt = str(input('Введите запись, которую нужно добавить в файл: '))
            if l != len(txt.split(' ')):
                ok = False
                print('Структура различается, повторите ввод...')
        for index in txt:
            f.write(index)
        f.write('\n')
        f.close()
        print()
        print('Запись добавлена в файл.')
        print()

    # (4) пункт
    if menu == 4:
        f = open(name, 'r')
        print()
        for line in f:
            st = line
            st = st[:-1]
            print(*st,sep='')
        f.close()

    # (5) пункт
    if menu == 5:
        f = open(name, 'r')
        l = f.readline()
        l = l.split(' ')
        print('Доступные поля: ')
        for i in range(len(l)):
            print(i + 1,'. ', l[i], sep='')
        print()
        pole = int(input('Введите номер нужного поля: '))
        krit = str(input('Введите критерий поиска: '))
        krit = krit.lower()
        print()
        ok = False
        f.close()
        f = open(name,'r')
        st = f.readline()
        print(*st,sep='')
        for line in f:
            buff = line[:-1]
            buff = buff.split(' ')
            if str(buff[pole - 1]).lower() == krit:
                print(line,end = '')
                ok = True
        if not ok:
            print('Нужные записи отсутствуют')
        f.close()
    # (6) пункт
    if menu == 6:
        f = open(name, 'r')
        l = f.readline()
        l = l.split(' ')
        print('Доступные поля: ')
        for i in range(len(l)):
            print(i + 1,'. ', l[i], sep='')
        print()
        pole1 = int(input('Введите номер первого нужного поля: '))
        pole2 = int(input('Введите номер второго нужного поля: '))
        krit1 = str(input('Введите критерий поиска для первого поля: '))
        krit2 = str(input('Введите критерий поиска для второго поля: '))
        krit1 = krit1.lower()
        krit2 = krit2.lower()
        print()
        ok = False
        f.close()
        f = open(name,'r')
        st = f.readline()
        for line in f:
            buff = line[:-1]
            buff = buff.split(' ')
            if str(buff[pole1 - 1]).lower() == krit1 and str(buff[pole2 - 1]).lower() == krit2:
                print(line,end = '')
                ok = True
        if not ok:
            print('Нужные записи отсутствуют')
        f.close()

print()
print('End')
print()

                
