import pygame
import  random

# initialize Pygame
pygame.init()

# Set Screen
width = 800
height = 400
screen = pygame.display.set_mode((width, height))

# Window Display Settings

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player

PlayerImage = pygame.image.load("spacecraft.png")
PlayerX = 370
PlayerY = 320
Xchange = 0
Ychange = 0

# Enemy 1

Enemy_1_Image = pygame.image.load("EnemyAlien.png")
Enemy_1_X = 370
Enemy_1_Y = 15
Enemy_1_Xchange = 0
Enemy_1_Ychange = 0


def Player(x, y):
    screen.blit(PlayerImage, (x, y))

def Enemy(x, y):
    screen.blit(Enemy_1_Image, (x, y))


# Game Loop

windowRunning = True

while windowRunning:

    screen.fill((100, 0, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Xchange = -.1
            if event.key == pygame.K_RIGHT:
                Xchange = .1
            if event.key == pygame.K_UP:
                Ychange = -.1
            if event.key == pygame.K_DOWN:
                Ychange = .1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Xchange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                Ychange = 0

    PlayerX += Xchange

    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736

    PlayerY += Ychange
    Enemy(Enemy_1_X, Enemy_1_Y)
    Player(PlayerX, PlayerY)
    pygame.display.update()
