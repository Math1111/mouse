import pygame
import random

# Цвета
RECTANGLE_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

# Переменные для рисования прямоугольника
top_left = (0, 0)
size = (0, 0)
dragging = False

# Список для хранения всех прямоугольников
rectangles = []

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            top_left = event.pos
            size = (0, 0)
            dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            right_bottom = event.pos
            size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])
            dragging = False

            # Создаём новый прямоугольник с случайным цветом
            rect = pygame.Rect(top_left, size)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            rectangles.append((rect, color))

        elif event.type == pygame.MOUSEMOTION and dragging:
            right_bottom = event.pos
            size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])

    # Отрисовка
    screen.fill(BACKGROUND_COLOR)

    # Рисуем текущий прямоугольник (если рисуем)
    if dragging:
        pygame.draw.rect(screen, RECTANGLE_COLOR, (top_left, size), 1)

    # Рисуем все сохранённые прямоугольники
    for rectangle, color in rectangles:
        pygame.draw.rect(screen, color, rectangle, 1)

    pygame.display.flip()

pygame.quit()