# Двойное время
# Воякин Алексей ИУ7-14б


# Определение дня недели по Григорианскому календарю
# https://lifehacker.ru/kakoj-den-nedeli/
def day(d,m,y):
    base = ['Суббота', 'Воскресенье' , 'Понедельник' , 'Вторник' ,
            'Среда' , 'Четверг' , 'Пятница']
    if (y >= 1600 and y < 1700) or (y >= 2000 and y < 2100):
        kod_veka = 6
    elif y >= 1700 and y < 1800:
        kod_veka = 4
    elif y >= 1800 and y < 1900:
        kod_veka = 2
    elif y >= 1900 and y < 2000:
        kod_veka = 0
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
    god_last2 = y - ((y // 100) * 100)
    kod_goda = (kod_veka + god_last2 + (god_last2 // 4)) % 7
    ind = (d + kod_goda + kod_mes) % 7
    if y % 4 == 0 and ind != 0 and ((d >= 0 and d <= 31 and m == 'Января') \
                                    or (d>=0 and d <= 29 and m == 'Февраля')) \
                                    and (y % 100 != 0 or y % 400 == 0):
        ind -= 1
    elif y % 4 == 0 and ind == 0 and ((d >= 0 and d <= 31 and m == 'Января') \
                                      or (d>=0 and d <= 29 and m == 'Февраля')) \
                                      and (y % 100 != 0 or y % 400 == 0):
        ind = 6
    return base[ind]


# Перевод из Юлианского в Григорианский
#https://ru.wikipedia.org/wiki/%D0%AE%D0%BB%D0%B8%D0%B0%
#D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%B0%D0%BB%D0%B5%D
#0%BD%D0%B4%D0%B0%D1%80%D1%8C
def to_grigo(d,m,y):
    kol_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    perevod = 10
    for i in range(1582, y):
        if i % 100 == 0 and i % 400 != 0:
            perevod += 1
    if (y % 100 != 0 or y % 400 == 0) or y % 4 == 0:
        kol_days[1] = 29
    d += perevod
    if d > kol_days[m - 1]:
        d -= kol_days[m - 1]
        m += 1
        if m > 12:
            m = 1
            y += 1
    return d, m, y



# Перевод из Григорианской в Юлианский
def to_ylian(d, m, y):
    kol_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    perevod = 10
    for i in range(1582, y):
        if i % 100 == 0 and i % 400 != 0:
            perevod += 1
    if (y % 100 != 0 or y % 400 == 0) or y % 4 == 0:
        kol_days[1] = 29
    d -= perevod
    if d <= 0:
        m -= 1
        if m ==0:
            y -= 1
            m = 12
        d += kol_days[m - 1]
    return d, m, y


# Выполнение программы
# http://www.direct-time.ru/%D0%BA%D0%BE%D0%BD%
##
m_name = {'Января': 1, 'Февраля': 2, 'Марта': 3,
           'Апреля': 4, 'Мая': 5, 'Июня': 6,
           'Июля': 7, 'Августа': 8, 'Сентября': 9,
           'Октября': 10, 'Ноября': 11, 'Декабря': 12}
m_return = {1: 'Января', 2: 'Февраля', 3: 'Марта',
            4: 'Апреля', 5: 'Мая', 6: 'Июня',
            7: 'Июля', 8: 'Августа', 9: 'Сентября',
            10: 'Октября', 11: 'Ноября', 12: 'Декабря'}
stor = []
txt = str(input())
while txt != '#':
    st = txt.split(' ')
    st[1] = int(st[1])
    st[2] = m_name[st[2]]
    st[3] = int(st[3])
    if st[0] != day(st[1], st[2], st[3]):
        st[1], st[2], st[3] = to_grigo(st[1], st[2], st[3])
    else:
        st[1], st[2], st[3] = to_ylian(st[1], st[2], st[3])
        st[1] = str(st[1])+'*'
    st[2] = m_return[st[2]]
    stor.append(st)
    txt = str(input())
for i in range(len(stor)):
    print(*stor[i])
