import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def check_collision_snake_and_apple(item1, item2):
    return item1[0] == item2[0] and item1[1] == item2[1]

def check_collision_snake_and_wall(item):
    return item[0] > 590 or item[0] < 0 or item[1] > 590 or item[1] < 0

def check_collision_snake_and_snake(item):
    return item[1:].count(item[0]) > 0

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220,200)]
snakeSkin = pygame.Surface((10,10))
snakeSkin.fill((255,255,255))
fastSnake = False

apple = pygame.Surface((10,10))
applePos = on_grid_random()
appleCounter = 0
apple.fill((255,0,0))

myDirection = LEFT

clock = pygame.time.Clock()

while True:

    if fastSnake:
        clock.tick(40)
    else:
        clock.tick(20)

    if check_collision_snake_and_wall(snake[0]):
        pygame.quit()

    if check_collision_snake_and_snake(snake):
        pygame.quit()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and myDirection != DOWN:
                myDirection = UP
            if event.key == K_DOWN and myDirection != UP:
                myDirection = DOWN
            if event.key == K_LEFT and myDirection != RIGHT:
                myDirection = LEFT
            if event.key == K_RIGHT and myDirection != LEFT:
                myDirection = RIGHT

    if check_collision_snake_and_apple(snake[0], applePos):
        appleCounter += 1

        if appleCounter % 5 == 0:
            snake.append([(0,0), (0,0), (0,0), (0,0), (0,0)])
            fastSnake = True
        else:
            snake.append((0,0))
            fastSnake = False

        if (appleCounter + 1) % 5 == 0:
            apple.fill((0,255,0))
        else:
            apple.fill((255,0,0))

        applePos = on_grid_random()

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if myDirection == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if myDirection == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if myDirection == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if myDirection == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0))
    
    screen.blit(apple, applePos)

    for pos in snake:
        screen.blit(snakeSkin,pos)

    pygame.display.update()