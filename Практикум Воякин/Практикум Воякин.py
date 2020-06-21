# Двойное время
# Воякин Алексей ИУ7-14б


# Определение дня недели по Григорианскому календарю
def day(d,m,y):
    base = ['Суббота', 'Воскресенье' , 'Понедельник' , 'Вторник' ,
            'Среда' , 'Четверг' , 'Пятница']
    
    # Определение кода века введённого года
    if (y >= 1600 and y < 1700) or (y >= 2000 and y < 2100):
        kod_veka = 6
    elif y >= 1700 and y < 1800:
        kod_veka = 4
    elif y >= 1800 and y < 1900:
        kod_veka = 2
    elif y >= 1900 and y < 2000:
        kod_veka = 0
        
    # Определение кода месяца
    if m == 4 or m == 7:
        kod_mes = 0
    elif m == 1 or m == 10:
        kod_mes = 1
    elif m == 5:
        kod_mes = 2
    elif m == 8:
        kod_mes = 3
    elif m == 2 or m == 3 or m == 11:
        kod_mes = 4
    elif m == 6:
        kod_mes = 5
    elif m == 12 or m == 9:
        kod_mes = 6
    god_last2 = y - ((y // 100) * 100)      # Определение последних двух цифр введённого года
    kod_goda = (kod_veka + god_last2 + (god_last2 // 4)) % 7      # Определение когда года
    ind = (d + kod_goda + kod_mes) % 7      # Определение номера полученного месяца

    # Смещение дня недели если год високосный и дата меньше 1 Марта
    if y % 4 == 0 and ind != 0 and ((d >= 0 and d <= 31 and m == 'Января') \
                                    or (d>=0 and d <= 29 and m == 'Февраля')) \
                                    and (y % 100 != 0 or y % 400 == 0):
        ind -= 1
    elif y % 4 == 0 and ind == 0 and ((d >= 0 and d <= 31 and m == 'Января') \
                                      or (d>=0 and d <= 29 and m == 'Февраля')) \
                                      and (y % 100 != 0 or y % 400 == 0):
        ind = 6

    # Возвращение дня недел текстом
    return base[ind]


# Перевод из Юлианского в Григорианский
def to_grigo(d,m,y):
    perevod = 10      # Начальная разница календарей

    # Нахождение разницы календарей для текущего года
    for i in range(1582, y + 1):
        if i % 100 == 0 and i % 400 != 0 and y != i:
            perevod += 1
        elif i % 100 == 0 and i % 400 != 0 and y == i and m != 1 and m != 2:
            perevod += 1
    # Изменение кол-ва дней Февраля в зависимости от високосности года
    if (y % 100 != 0 or y % 400 == 0) and y % 4 == 0:
        kol_days[1] = 29
    else:
        kol_days[1] = 28
    d += perevod
    if d > kol_days[m - 1]:
        d -= kol_days[m - 1]
        m += 1
        if m > 12:
            m = 1
            y += 1
    return d, m, y



# Перевод из Григорианского в Юлианский
def to_ylian(d, m, y):
    perevod = 10      # Начальная разница календарей

    # Нахождение разницы календарей для текущего года
    for i in range(1582, y + 1):
        if i % 100 == 0 and i % 400 != 0 and y != i:
            perevod += 1
        elif i % 100 == 0 and i % 400 != 0 and y == i and m != 1 and m != 2:
            perevod += 1
    # Изменение кол-ва дней Февраля в зависимости от високосности года        
    if y % 4 == 0:
        kol_days[1] = 29
    else:
        kol_days[1] = 28
    d -= perevod
    if d <= 0:
        m -= 1
        if m ==0:
            y -= 1
            m = 12
        d += kol_days[m - 1]
    return d, m, y


# Выполнение программы
m_name = {'Января': 1, 'Февраля': 2, 'Марта': 3,
           'Апреля': 4, 'Мая': 5, 'Июня': 6,
           'Июля': 7, 'Августа': 8, 'Сентября': 9,
           'Октября': 10, 'Ноября': 11, 'Декабря': 12}
m_return = {1: 'Января', 2: 'Февраля', 3: 'Марта',
            4: 'Апреля', 5: 'Мая', 6: 'Июня',
            7: 'Июля', 8: 'Августа', 9: 'Сентября',
            10: 'Октября', 11: 'Ноября', 12: 'Декабря'}
kol_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
stor = []
print('Введите день недели, день, месяц, год: ')
print('Символ # чтобы закончить ввод')      
txt = str(input())
while txt != '#':
    txt = txt.split(' ')
    txt[1] = int(txt[1])
    txt[2] = m_name[txt[2]]      # Перевод текствого месяца в цифровой
    txt[3] = int(txt[3])
    if txt[3] % 400 != 0:
        # Перевод в другой календарь 
        if txt[0] != day(txt[1], txt[2], txt[3]):
            txt[1], txt[2], txt[3] = to_grigo(txt[1], txt[2], txt[3])
        else:
            txt[1], txt[2], txt[3] = to_ylian(txt[1], txt[2], txt[3])
            txt[1] = str(txt[1])+'*'

        # Возврат месяца текстом
        txt[2] = m_return[txt[2]]
        stor.append(txt)
    else:
        stor.append(0)
    txt = str(input())
    
# Вывод полученных дат
print('Даты после перевода в другой календарь: ')
for i in range(len(stor)):
    if stor[i] == 0:
        print('Определить календарь для данного года невозможно')
    else:
        print(*stor[i])
