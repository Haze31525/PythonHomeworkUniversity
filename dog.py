import pygame
import sys
import random


def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def draw_trace(cur_screen, tail, color):
    for i in range(len(tail) - 1):
        y1, x1, y2, x2 = *tail[i], *tail[i + 1]
        x1 = x1 * 20 + 5
        x2 = x2 * 20 + 5
        y1 = y1 * 20 + 5
        y2 = y2 * 20 + 5
        rect = pygame.Rect(min(x1, x2), min(y1, y2), 10 + abs(x1 - x2), 10 + abs(y1 - y2))
        pygame.draw.rect(cur_screen, color, rect)


def draw_dog(cur_screen, pos, color):
    x = pos[1] * 20 + 10
    y = pos[0] * 20 + 10
    pygame.draw.circle(cur_screen, color, (x, y), 9)


def main_game():
    global screen, start, SPEED, field, old_tails
    x, y = start
    trace = [(x, y)]
    field[x][y] = 1
    timer = 0
    dmove = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while True:
        close_game()
        timer += clock.tick()
        if timer >= SPEED:
            if x == 0 or x == SIZE - 1 or y == 0 or y == SIZE - 1:
                return (x, y), trace, False
            if field[x + 1][y] and field[x - 1][y] and field[x][y + 1] and field[x][y - 1]:
                return (x, y), trace, True
            direction = random.choice([el for el in dmove if not field[x + el[0]][y + el[1]]])
            x += direction[0]
            y += direction[1]
            field[x][y] = 1
            trace.append((x, y))
            screen.fill(pygame.Color('black'))
            for el in old_tails:
                draw_trace(screen, el, color_trail)
            draw_trace(screen, trace, color_trail)
            draw_dog(screen, (x, y), color)
            pygame.display.flip()
            timer = 0


def game_over(pos):
    global field, start, screen, old_tails

    spawn = random.randint(0, SIZE * 20 - 10)
    coords = [(0, spawn), (SIZE * 20 - 10, spawn), (spawn, 0), (spawn, SIZE * 20 - 10)]
    spawn = coords[random.randint(0, 3)]
    x, y = spawn
    dir_y, dir_x = pos[0] * 20 + 10 - y, pos[1] * 20 + 10 - x
    save_speed = (dir_x ** 2 + dir_y ** 2) ** 0.5 * 5
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 6)
    pygame.display.flip()
    while abs(x - pos[1] * 20 - 10) > 2 or abs(y - pos[0] * 20 - 10) > 2:
        close_game()
        change = clock.tick()
        x += dir_x * change / save_speed
        y += dir_y * change / save_speed
        screen.fill(pygame.Color('black'))
        for el in old_tails:
            draw_trace(screen, el, color_trail)
        draw_dog(screen, pos, color)
        pygame.draw.circle(screen, pygame.Color('red'), (x, y), 6)
        pygame.display.flip()

    while field[pos[0]][pos[1]]:
        pos = (random.randint(0, SIZE - 1), random.randint(0, SIZE - 1))
    dir_y, dir_x = pos[0] * 20 + 10 - y, pos[1] * 20 + 10 - x
    save_speed = (dir_x ** 2 + dir_y ** 2) ** 0.5 * 5
    while abs(x - pos[1] * 20 - 10) > 2 or abs(y - pos[0] * 20 - 10) > 2:
        close_game()
        change = clock.tick()
        x += dir_x * change / save_speed
        y += dir_y * change / save_speed
        screen.fill(pygame.Color('black'))
        for el in old_tails:
            draw_trace(screen, el, color_trail)
        pygame.draw.circle(screen, color, (x, y), 9)
        pygame.draw.circle(screen, pygame.Color('red'), (x, y), 6)
        pygame.display.flip()
    dir_y, dir_x = spawn[1] - y, spawn[0] - x
    save_speed = (dir_x ** 2 + dir_y ** 2) ** 0.5 * 5
    while SIZE * 20 > x > 0 and SIZE * 20 > y > 0:
        close_game()
        change = clock.tick()
        x += dir_x * change / save_speed
        y += dir_y * change / save_speed
        screen.fill(pygame.Color('black'))
        for el in old_tails:
            draw_trace(screen, el, color_trail)
        draw_dog(screen, pos, color)
        pygame.draw.circle(screen, pygame.Color('red'), (x, y), 6)
        pygame.display.flip()
    start = pos
    screen.fill(pygame.Color('black'))
    for el in old_tails:
        draw_trace(screen, el, color_trail)
    draw_dog(screen, pos, color)
    pygame.display.flip()
    pygame.time.wait(SPEED)


def win(pos):
    global screen, field, start, old_tails
    start = (SIZE // 2, SIZE // 2)
    field = [[0] * SIZE for _ in range(SIZE)]
    old_tails = []
    pygame.draw.circle(screen, pygame.Color('black'), (pos[1] * 20 + 6, pos[0] * 20 + 8), 1)
    pygame.draw.circle(screen, pygame.Color('black'), (pos[1] * 20 + 14, pos[0] * 20 + 8), 1)
    pygame.draw.arc(screen, pygame.Color('black'), (pos[1] * 20 + 4, pos[0] * 20 + 10, 12, 6), 3.14, 6.3)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                screen.fill(pygame.Color('black'))
                draw_dog(screen, start)
                pygame.display.flip()
                pygame.time.wait(SPEED)

                return


pygame.init()
old_tails = []
SIZE = 30
SPEED = 200
screen = pygame.display.set_mode((SIZE * 20, SIZE * 20))
clock = pygame.time.Clock()
start = (SIZE // 2, SIZE // 2)
field = [[0] * SIZE for _ in range(SIZE)]
color = pygame.Color('orange')
color_trail = pygame.Color('white')

while True:
    coord, taken, lost = main_game()
    old_tails.append(taken)
    if lost:
        game_over(coord)
    else:
        # game_over(coord)
        win(coord)
