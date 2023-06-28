import pygame
import os
from random import randint
from math import *

pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")  # Title
icon = pygame.image.load("snake.png")
pygame.display.set_icon(icon)

head_x = 300
head_y = 300
snake_size = 20
velx = []
vely = []

food_x = -1
food_y = -1
while food_x % 5 != 0:
    food_x = randint(40, 460)
while food_y % 5 != 0:
    food_y = randint(40, 460)

score = 0
snake = []
turn = [[-1, -1]]

for i in range(0, snake_size):
    snake.append([head_x - i * 8, head_y])
    velx.append(8)
    vely.append(0)

turn_complete = [False]
running = True


def drawfood(x, y, width, height, r, g, b):
    pygame.draw.rect(screen, (r, g, b), (x, y, width, height))


def drawsnake(snake, snake_size):
    global velx
    global vely
    r = 46
    g = 139
    b = 87


    for i in range(0, snake_size):
        pygame.draw.rect(screen, (r, g, b), (snake[i][0], snake[i][1], 7, 7))


def is_game_over(snake):
    for i in range(1, len(snake)):
        dis = sqrt(pow(snake[0][0] - snake[i][0], 2) + pow(snake[0][1] - snake[i][1], 2))
        if dis <= 4:
            return True

    return False



while running:
    pygame.time.delay(45)
    screen.fill((255, 255, 255))  # RGB

    if is_game_over(snake):
        pygame.quit()
        break

    drawsnake(snake, snake_size)
    for j in range(0, len(turn)):
        if turn_complete[j]:
            turn[j] = [-1, -1]
            turn_complete[j] = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT and velx[0] != -8:
                velx[0] = 8
                vely[0] = 0

                if [-1, -1] in turn:
                    turn.remove([-1, -1])
                else:
                    turn_complete.append(False)

                turn.append([snake[0][0], snake[0][1]])
                break

            if event.key == pygame.K_LEFT and velx[0] != 8:
                velx[0] = -8
                vely[0] = 0

                if [-1, -1] in turn:
                    turn.remove([-1, -1])
                else:
                    turn_complete.append(False)

                turn.append([snake[0][0], snake[0][1]])
                break

            if event.key == pygame.K_UP and vely[0] != 8:
                vely[0] = -8
                velx[0] = 0

                if [-1, -1] in turn:
                    turn.remove([-1, -1])
                else:
                    turn_complete.append(False)

                turn.append([snake[0][0], snake[0][1]])
                break

            if event.key == pygame.K_DOWN and vely[0] != -8:
                vely[0] = 8
                velx[0] = 0

                if [-1, -1] in turn:
                    turn.remove([-1, -1])
                else:
                    turn_complete.append(False)

                turn.append([snake[0][0], snake[0][1]])
                break

    for i in range(0, snake_size):
        if snake[i][0] < 10:
            snake[i][0] = 490
        if snake[i][0] > 490:
            snake[i][0] = 10
        if snake[i][1] < 10:
            snake[i][1] = 490
        if snake[i][1] > 490:
            snake[i][1] = 10

        snake[i][0] += velx[i]
        snake[i][1] += vely[i]




    for j in range(0, len(turn)):
        for i in range(1, snake_size):

            if velx[i - 1] != 0 and snake[i] == turn[j]:
                velx[i] = velx[i - 1]
                vely[i] = 0
            if vely[i - 1] != 0 and snake[i] == turn[j]:
                vely[i] = vely[i - 1]
                velx[i] = 0
            if snake[snake_size - 1] == turn[j]:
                turn_complete[j] = True




    drawfood(food_x, food_y, 8, 8, 255, 0, 0)

    d = sqrt(pow(snake[0][0] - food_x, 2) + pow(snake[0][1] - food_y, 2))
    if d <= 8:
        drawfood(food_x, food_y, 8, 8, 255, 255, 255)
        score += 10
        food_x = -1
        food_y = -1
        snake_size += 1
        velx.append(velx[snake_size - 2])
        vely.append(vely[snake_size - 2])
        snake.append([snake[snake_size - 2][0] - velx[snake_size - 2], snake[snake_size - 2][1] - vely[snake_size - 2]])
        while food_x % 5 != 0:
            food_x = randint(40, 460)
        while food_y % 5 != 0:
            food_y = randint(40, 460)



    pygame.display.update()
