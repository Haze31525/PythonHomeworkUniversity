import sys
import random
import pygame


class Node:
    def __init__(self, parent, pos, g, finish):
        self.parent = parent
        self.coord = pos
        self.g = g
        self.h = abs(pos[0] - finish[0]) + abs(pos[1] - finish[1])
        self.f = g + self.h

    def __eq__(self, other):
        return self.f == other.f

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def __gt__(self, other):
        return self.f > other.f

    def __ge__(self, other):
        return self.f >= other.f


# Задание размера поля и частоту расстановки стен
def init():
    print('Введите размер поля в клетках')
    size = int(input())
    print('Введите размер клетки')
    cell = int(input())
    print('Введите частоту расстановки стен (от 0 до 1)')
    freq = float(input())
    field = [[0 if random.random() >= freq else 1 for _ in range(size)] for _ in range(size)]
    field[0][0] = 0
    return size, cell, field


# создание рандомного поля
def draw_field(screen, field, size, cell, color, color_sep, color_screen):
    screen.fill(color_screen)
    for i in range(size):
        for j in range(size):
            if field[i][j]:
                wall = pygame.Rect(j * cell, i * cell, cell, cell)
                pygame.draw.rect(screen, color, wall)
    for i in range(size - 1):
        line = pygame.Rect((i + 1) * cell, 0, 1, cell * size)
        pygame.draw.rect(screen, color_sep, line)
        line = pygame.Rect(0, (i + 1) * cell, cell * size, 1)
        pygame.draw.rect(screen, color_sep, line)
    pygame.display.flip()


# выбор старта/финиша, ждет нажатия клавиши
def positions(screen, field, cell, start, finish, color_s, color_f, color_screen):
    new = pygame.Rect(finish[1] * cell + 1, finish[0] * cell + 1, cell - 1, cell - 1)
    pygame.draw.rect(screen, color_f, new)
    new = pygame.Rect(start[1] * cell + 1, start[0] * cell + 1, cell - 1, cell - 1)
    pygame.draw.rect(screen, color_s, new)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                presses = pygame.mouse.get_pressed()
                y, x = pygame.mouse.get_pos()
                y //= cell
                x //= cell
                if not field[x][y]:
                    if presses[2]:
                        old = pygame.Rect(start[1] * cell + 1, start[0] * cell + 1, cell - 1, cell - 1)
                        pygame.draw.rect(screen, color_screen, old)
                        start = (x, y)
                    elif presses[0]:
                        old = pygame.Rect(finish[1] * cell + 1, finish[0] * cell + 1, cell - 1, cell - 1)
                        pygame.draw.rect(screen, color_screen, old)
                        finish = (x, y)

                    new = pygame.Rect(finish[1] * cell + 1, finish[0] * cell + 1, cell - 1, cell - 1)
                    pygame.draw.rect(screen, color_f, new)
                    new = pygame.Rect(start[1] * cell + 1, start[0] * cell + 1, cell - 1, cell - 1)
                    pygame.draw.rect(screen, color_s, new)
                    pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                return start, finish


# сам A*
def find_way(field, start, finish, size):
    checked = [[0 for _ in range(size)] for _ in range(size)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = [Node((-1, -1), start, 0, finish)]

    while queue:
        cur = min(queue)
        queue.remove(cur)
        x, y = cur.coord
        checked[x][y] = cur.parent
        if cur.coord == finish:
            return get_way(checked, start, finish)
        for i in range(4):
            if 0 <= x + dx[i] < size and 0 <= y + dy[i] < size:
                if not field[x + dx[i]][y + dy[i]]:
                    new = True
                    if not checked[x + dx[i]][y + dy[i]]:
                        for el in queue:
                            if el.coord == (x + dx[i], y + dy[i]):
                                if el.g > cur.g + 1:
                                    el.g = cur.g + 1
                                    el.parent = cur.coord
                                    el.f = el.h + el.g
                                new = False
                        if new:
                            queue.append(Node(cur.coord, (x + dx[i], y + dy[i]), cur.g + 1, finish))
    return 0


# находит какой мы получили путь по A* и сохраняет в массив
def get_way(field, start, finish):
    way = [finish]
    while way[-1] != start:
        x, y = way[-1]
        way.append(field[x][y])
    way.reverse()
    return way


# отрисовывает путь
def visualize(screen, way, cell, speed, color, color_screen):
    for el in way:
        new = pygame.Rect(el[1] * cell + 1, el[0] * cell + 1, cell - 1, cell - 1)
        pygame.draw.rect(screen, color, new)
        pygame.display.flip()
        pygame.time.wait(speed)
    for el in way[:-1]:
        new = pygame.Rect(el[1] * cell + 1, el[0] * cell + 1, cell - 1, cell - 1)
        pygame.draw.rect(screen, color_screen, new)
        pygame.display.flip()
        pygame.time.wait(speed)


# если нет пути
def no_way(screen, start, cell, speed, color_a, color_b):
    for i in range(3):
        new = pygame.Rect(start[1] * cell + 1, start[0] * cell + 1, cell - 1, cell - 1)
        pygame.draw.rect(screen, color_b, new)
        pygame.display.flip()
        pygame.time.wait(speed)
        new = pygame.Rect(start[1] * cell + 1, start[0] * cell + 1, cell - 1, cell - 1)
        pygame.draw.rect(screen, color_a, new)
        pygame.display.flip()
        pygame.time.wait(speed)


def main():
    pygame.init()
    SPEED = 30
    S_FLASH = 200
    colors = {'field': pygame.Color('white'), 'main': pygame.Color('red'),
              'finish': pygame.Color('green'), 'sep': pygame.Color('grey'),
              'wall': pygame.Color('black'), 'extra': pygame.Color('yellow')}
    SIZE, CELL, field = init()
    screen = pygame.display.set_mode((SIZE * CELL, SIZE * CELL))
    draw_field(screen, field, SIZE, CELL, colors['wall'], colors['sep'], colors['field'])
    start, finish = (0, 0), (0, 0)
    while True:
        start, finish = positions(screen, field, CELL, start, finish, colors['main'], colors['finish'], colors['field'])
        way = find_way(field, start, finish, SIZE)
        if way:
            visualize(screen, way, CELL, SPEED, colors['main'], colors['field'])
            start = finish
        else:
            no_way(screen, start, CELL, S_FLASH, colors['main'], colors['extra'])


# ПКМ по клетке - начало пути
# ЛКМ по клетке - конец пути
# любая клавиша - начать поиск пути
main()
