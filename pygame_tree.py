import pygame
import random
from math import cos, sin
pygame.init()


# Получение повернутой координаты X
def xn(x_start, y_start, alpha_vent, x_center, y_center):
    return int(-sin(alpha_vent) * (y_start - y_center) + cos(alpha_vent) * (x_start - x_center) + x_center)


# Получение повернутой координаты Y
def yn(x_start, y_start, alpha_vent, x_center, y_center):
    return int(cos(alpha_vent) * (y_start - y_center) + sin(alpha_vent) * (x_start - x_center) + y_center)


# Главная программа
def main():
    # Размер окна
    WIN_WIDTH = 1000
    WIN_HEIGHT = 600
    clock = pygame.time.Clock()
    FPS = 60
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    # Параметры для вращения вертушки
    alpha_vent = 0
    alpha_koef = -350
    mi = 1
    koleb = 5
    m = 2
    r1, r2, r3, r4, r5, r6, r7, r8 = 0, 0, 0, 0, 0, 0, 0, 0
    do_rand = 1
    r_ok1, r_ok2, r_ok3, r_ok4, r_ok5, r_ok6, r_ok7, r_ok8 = 0, 0, 0, 0, 0, 0, 0, 0
    koleb1, koleb2, koleb3, koleb4, koleb5, koleb6, koleb7, koleb8 = 0, 0, 0, 0, 0, 0, 0, 0
    r = -1
    # Построение и обновление экрана
    while True:
        clock.tick(FPS)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                return
        window.fill((185, 220, 225))
        # Поляна и столб вертушки
        pygame.draw.ellipse(window, (100, 161, 82), (-WIN_WIDTH / 4, WIN_HEIGHT / 4, WIN_WIDTH * 1.5, WIN_HEIGHT))
        # Отрисовка дерева
        if koleb <= 10 and koleb >= 0:
            koleb += 0.1 * m
        else:
            m *= -1
            koleb += 0.1* m
        # Ветки
        pygame.draw.polygon(window, (92, 69, 42), [[380, 330], [420, 250], [460, 330]])
        pygame.draw.lines(window, (92, 69, 42), True, [[420, 270], [420, 50]], 10)
        pygame.draw.polygon(window, (92, 69, 42), [[390, 330], [420, 230], [450, 330]])
        pygame.draw.arc(window, (92, 69, 42), (330, 50, 180, 180 - 4 * koleb), 3.14 * 0, 0.5 * 3.14, 7)
        pygame.draw.arc(window, (92, 69, 42), (330, 50, 180, 180 + 4 * koleb), 3.14 * 0.5, 1 * 3.14, 7)
        pygame.draw.arc(window, (92, 69, 42), (370, 150, 100, 180 + 4 * koleb), 3.14 * 0, 0.5 * 3.14, 7)
        pygame.draw.arc(window, (92, 69, 42), (370, 150, 100, 180 - 4 * koleb), 3.14 * 0.5, 1 * 3.14, 7)
        # Статическая листва
        pygame.draw.circle(window, (127, 189, 52), (420, 55), 20)
        pygame.draw.circle(window, (127, 189, 52), (402, 93), 17)
        pygame.draw.circle(window, (77, 144, 34), (441, 107), 17)
        pygame.draw.circle(window, (127, 189, 52), (407, 125), 13)
        pygame.draw.circle(window, (127, 189, 52), (433, 140), 10)
        pygame.draw.circle(window, (77, 144, 34), (410, 155), 9)
        pygame.draw.circle(window, (127, 189, 52), (425, 170), 7)
        # Динамическая листва лево верх
        pygame.draw.circle(window, (127, 189, 52), (333, int(145 + 2 * koleb)), 14)
        pygame.draw.circle(window, (127, 189, 52), (344, int(175 + 2 * koleb)), 10)
        pygame.draw.circle(window, (127, 189, 52), (335, int(194 + 2 * koleb)), 9)
        pygame.draw.circle(window, (127, 189, 52), (322, int(209 + 2 * koleb)), 8)
        pygame.draw.circle(window, (127, 189, 52), (333, int(230 + 2 * koleb)), 6)
        # Динамическая листва право верх
        pygame.draw.circle(window, (127, 189, 52), (507, int(145 - 2 * koleb)), 14)
        pygame.draw.circle(window, (127, 189, 52), (518, int(175 - 2 * koleb)), 10)
        pygame.draw.circle(window, (127, 189, 52), (509, int(194 - 2 * koleb)), 9)
        pygame.draw.circle(window, (127, 189, 52), (496, int(209 - 2 * koleb)), 8)
        pygame.draw.circle(window, (127, 189, 52), (507, int(230 - 2 * koleb)), 6)
        # Динамическая листва лево низ
        pygame.draw.circle(window, (127, 189, 52), (375, int(230 - 2 * koleb)), 12)
        pygame.draw.circle(window, (127, 189, 52), (364, int(252 - 2 * koleb)), 10)
        pygame.draw.circle(window, (127, 189, 52), (377, int(269 - 2 * koleb)), 7)
        pygame.draw.circle(window, (127, 189, 52), (378, int(286 - 2 * koleb)), 5)
        pygame.draw.circle(window, (127, 189, 52), (373, int(296 - 2 * koleb)), 4)
        # Динамическая листва право низ
        pygame.draw.circle(window, (127, 189, 52), (467, int(230 + 2 * koleb)), 12)
        pygame.draw.circle(window, (127, 189, 52), (456, int(252 + 2 * koleb)), 10)
        pygame.draw.circle(window, (127, 189, 52), (469, int(269 + 2 * koleb)), 7)
        pygame.draw.circle(window, (127, 189, 52), (470, int(286 + 2 * koleb)), 5)

        if do_rand == 1:
            buff = r
            while buff == r:
                buff = random.randint(1,8)
            r = buff

            if r == 1 and r_ok1 == 0:
                r_ok1 = 1
            elif r == 2 and r_ok2 == 0:
                r_ok2 = 1
            elif r == 3 and r_ok3 == 0:
                r_ok3 = 1
            elif r == 4 and r_ok4 == 0:
                r_ok4 = 1
            elif r == 5 and r_ok5 == 0:
                r_ok5 = 1
            elif r == 6 and r_ok6 == 0:
                r_ok6 = 1
            elif r == 7 and r_ok7 == 0:
                r_ok7 = 1
            elif r == 8 and r_ok8 == 0:
                r_ok8 = 1
            do_rand = 0

        if r_ok1 == 1:
            r1 += 1
            pygame.draw.circle(window, (77, 144, 34), (320, int(171 + 2 * koleb)), int (12 * r1 / 140))
            if r1 == 140:
                r1 = 0
                do_rand = 1
                r_ok1 = 0
                koleb1 = koleb
        else:
            koleb1 = koleb
        if r_ok2 == 1:
            r2 += 1
            pygame.draw.circle(window, (77, 144, 34), (337, int(215 + 2 * koleb)), int(7 * r2 / 100))
            if r2 == 100:
                r2 = 0
                do_rand = 1
                r_ok2 = 0
                koleb2 = koleb
        else:
            koleb2 = koleb
        if r_ok3 == 1:
            r3 += 1
            pygame.draw.circle(window, (77, 144, 34), (494, int(171 - 2 * koleb)), int(12 * r3 / 140))
            if r3 == 140:
                r3 = 0
                do_rand = 1
                r_ok3 = 0
                koleb3 = koleb
        else:
            koleb3 = koleb
        if r_ok4 == 1:
            r4 += 1
            pygame.draw.circle(window, (77, 144, 34), (511, int(215 - 2 * koleb)), int(7 * r4 / 100))
            if r4 == 100:
                r4 = 0
                do_rand = 1
                r_ok4 = 0
                koleb4 = koleb
        else:
            koleb4 = koleb
        if r_ok5 == 1:
            r5 += 1
            pygame.draw.circle(window, (77, 144, 34), (383, int(255 - 2 * koleb)), int(8 * r5 / 65))
            if r5 == 65:
                r5 = 0
                do_rand = 1
                r_ok5 = 0
                koleb5 = koleb
        else:
            koleb5 = koleb
        if r_ok6 == 1:
            r6 += 1
            pygame.draw.circle(window, (77, 144, 34), (367, int(280 - 2 * koleb)), int(6 * r6 / 50))
            if r6 == 50:
                r6 = 0
                do_rand = 1
                r_ok6 = 0
                koleb6 = koleb
        else:
            koleb6 = koleb
        if r_ok7 == 1:
            r7 += 1
            pygame.draw.circle(window, (77, 144, 34), (475, int(255 + 2 * koleb)), int(8 * r7 / 70))
            if r7 == 70:
                r7 = 0
                do_rand = 1
                r_ok7 = 0
                koleb7 = koleb
        else:
            koleb7 = koleb
        if r_ok8 == 1:
            r8 += 1
            pygame.draw.circle(window, (77, 144, 34), (459, int(280 + 2 * koleb)), int(6 * r8 / 50))
            if r8 == 50:
                r8 = 0
                do_rand = 1
                r_ok8 = 0
                koleb8 = koleb
        else:
            koleb8 = koleb


        pygame.draw.ellipse(window, (51, 89, 34),
                            (-WIN_WIDTH / 4 + 150, WIN_HEIGHT / 4 + 140, WIN_WIDTH * 1.8, WIN_HEIGHT))
        pygame.draw.line(window, (131, 73, 37), [90, WIN_HEIGHT / 2 + 30], [90, WIN_HEIGHT], 9)

        # Листва летающая
        pygame.draw.circle(window, (77, 144, 34), (320 + int(r1 * 3 * alpha_vent / 26), int(171 + r1 + 2 * koleb1)), int(12 - 12 * r1 / 140))
        pygame.draw.circle(window, (77, 144, 34), (337 + int(r2 * 3 * alpha_vent / 26), int(215 + r2 + 2 * koleb2)), int(7 - 7 * r2 /100))
        pygame.draw.circle(window, (77, 144, 34), (494 + int(r3 * 3 * alpha_vent / 26), int(171 + r3 - 2 * koleb3)), int(12 - 12 * r3 / 140))
        pygame.draw.circle(window, (77, 144, 34), (511 + int(r4 * 3 * alpha_vent / 26), int(215 + r4 - 2 * koleb4)), int(7 - 7 * r4 / 100))
        pygame.draw.circle(window, (77, 144, 34), (383 + int(r5 * 3 * alpha_vent / 26), int(255 + r5 - 2 * koleb5)), int(8 - 8 * r5 / 65))
        pygame.draw.circle(window, (77, 144, 34), (367 + int(r6 * 3 * alpha_vent / 26), int(280 + r6 - 2 * koleb6)), int(6 - 6 * r6 / 50))
        pygame.draw.circle(window, (77, 144, 34), (475 + int(r7 * 3 * alpha_vent / 26), int(255 + r7 + 2 * koleb7)), int(8 - 8 * r7 / 70))
        pygame.draw.circle(window, (77, 144, 34), (459 + int(r8 * 3 * alpha_vent / 26), int(280 + r8 + 2 * koleb8)), int(6 - 6 * r8 / 50))

        pygame.draw.ellipse(window, (138, 155, 56), (-WIN_WIDTH / 4, WIN_HEIGHT / 4 + 250, WIN_WIDTH * 1.4, WIN_HEIGHT))
        # Квадрат вертушки
        pygame.draw.polygon(window, (20, 86, 165), [[xn(150, 330, alpha_vent, 90, 330), yn(150, 330, alpha_vent, 90, 330)],
            [xn(90, 390, alpha_vent, 90, 330), yn(90, 390, alpha_vent, 90, 330)],
            [xn(30, 330, alpha_vent, 90, 330), yn(30, 330, alpha_vent, 90, 330)],
            [xn(90, 270, alpha_vent, 90, 330), yn(90, 270, alpha_vent, 90, 330)]])
        # Лопасти вертушки
        pygame.draw.polygon(window, (35, 145, 212), [[90, 330], [xn(150, 330, alpha_vent, 90, 330),
            yn(150, 330, alpha_vent, 90, 330)], [xn(150, 390, alpha_vent, 90, 330), yn(150, 390, alpha_vent, 90, 330)]])
        pygame.draw.polygon(window, (35, 145, 212), [[90, 330], [xn(90, 390, alpha_vent, 90, 330),
            yn(90, 390, alpha_vent, 90, 330)], [xn(30, 390, alpha_vent, 90, 330), yn(30, 390, alpha_vent, 90, 330)]])
        pygame.draw.polygon(window, (35, 145, 212), [[90, 330], [xn(30, 330, alpha_vent, 90, 330),
            yn(30, 330, alpha_vent, 90, 330)], [xn(30, 270, alpha_vent, 90, 330), yn(30, 270, alpha_vent, 90, 330)]])
        pygame.draw.polygon(window, (35, 145, 212), [[90, 330], [xn(90, 270, alpha_vent, 90, 330),
            yn(90, 270, alpha_vent, 90, 330)], [xn(150, 270, alpha_vent, 90, 330), yn(150, 270, alpha_vent, 90, 330)]])
        # Центр вертушки
        pygame.draw.circle(window, (132, 179, 223), (90, 330), 10)
        # Поворот угла вертушки
        alpha_vent += 0.001 * alpha_koef
        if alpha_koef != 350 * mi:
            alpha_koef += 2 * mi
        else:
            mi *= -1
        # Обновление экрана
        pygame.display.update()


# запуск выполнения мейна
if __name__ == "__main__":
    main()
