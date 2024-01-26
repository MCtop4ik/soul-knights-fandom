# import pygame
# import sys
#
# def draw_rhombus(surface, color, x, y, size):
#     pygame.draw.polygon(surface, color, [
#         (x, y - size // 2),
#         (x + size // 2, y),
#         (x, y + size // 2),
#         (x - size // 2, y)
#     ])
#
# def main():
#     # Инициализация Pygame
#     pygame.init()
#
#     # Запрос ввода размера n
#     try:
#         n = int(input("Введите целое число n: "))
#     except ValueError:
#         print("Неправильный формат ввода")
#         sys.exit()
#
#     # Размеры окна
#     window_size = (300, 300)
#
#     # Создание окна
#     window = pygame.display.set_mode(window_size)
#     pygame.display.set_caption("Оранжевые ромбики на желтом фоне")
#
#     # Оранжевый и желтый цвета
#     orange_color = (255, 165, 0)
#     yellow_color = (255, 255, 0)
#
#     # Основной цикл программы
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#
#         # Очистка экрана желтым цветом
#         window.fill(yellow_color)
#
#         # Рисование оранжевых ромбиков
#         for i in range(n):
#             for j in range(n):
#                 x = (j + 1) * window_size[0] // (n + 1)
#                 y = (i + 1) * window_size[1] // (n + 1)
#                 draw_rhombus(window, orange_color, x, y, window_size[0] // (n + 1))
#
#         # Обновление экрана
#         pygame.display.flip()
#
#
# if __name__ == "__main__":
#     main()


import re

n, k = map(int, input().split())
real_codes = []
wrong_codes = []
for i in range(n):
    code = input()
    real_codes.append(code)
for i in range(k):
    code = input()
    wrong_codes.append(code)


def solve(n, k, real_codes, wrong_codes):
    def match_pattern(code):
        pattern = re.compile('[0-9]{4}[abc]-[a-z]{3}[0-9]{6}')
        return pattern.fullmatch(code) is not None

    TP = 0
    FP = 0
    FN = 0
    TN = 0
    for code in real_codes:
        if match_pattern(code):
            TP += 1
        else:
            FN += 1
    for code in wrong_codes:
        if match_pattern(code):
            FP += 1
        else:
            TN += 1
    print("{:.4f} {:.4f}".format(TP / (TP + FN), TP / (TP + FP)))


solve(n, k, real_codes, wrong_codes)
