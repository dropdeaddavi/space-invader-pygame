import pygame
import random
import math

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
Enemy_1_X = random.randint(0, 735)
Enemy_1_Y = random.randint(15, 100)
Enemy_1_Xchange = 0.1
Enemy_1_Ychange = 25

# Bullet

BulletImage = pygame.image.load("missile.png")
BulletX = 0
BulletY = 320
BulletXchange = 0
BulletYchange = .5
BulletState = "ready"

# Background

background = pygame.image.load("SpaceBackground.jpeg")


def Player(x, y):
    screen.blit(PlayerImage, (x, y))


def Enemy(x, y):
    screen.blit(Enemy_1_Image, (x, y))


def Fire_Bullet(x, y):
    global BulletState
    BulletState = "fire"
    screen.blit(BulletImage, (x + 16, y + 10))


def isCollision(Enemy_1_X, BulletX, Enemy_1_Y, BulletY):
    distance = math.sqrt(math.pow(Enemy_1_X - BulletX, 2) + math.pow(Enemy_1_Y - BulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop

windowRunning = True

while windowRunning:

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Xchange = -.1
            if event.key == pygame.K_RIGHT:
                Xchange = .1

            # Firing the bullet
            if event.key == pygame.K_SPACE:
                if BulletState == "ready":
                    BulletX = PlayerX
                    Fire_Bullet(BulletX, BulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Xchange = 0

    # Enemy Movement

    Enemy_1_X += Enemy_1_Xchange

    if Enemy_1_X <= 0:
        Enemy_1_Xchange = .1
        Enemy_1_Y += Enemy_1_Ychange
    elif Enemy_1_X >= 736:
        Enemy_1_Xchange = -.1
        Enemy_1_Y += Enemy_1_Ychange

    # Player Movement

    PlayerX += Xchange

    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736

    # Bullet Movement
    if BulletY <= 0:
        BulletY = 320
        BulletState = "ready"

    if BulletState == "fire":
        Fire_Bullet(BulletX, BulletY)
        BulletY -= BulletYchange

    # Collision Detection
    collision = isCollision(Enemy_1_X, BulletX, Enemy_1_Y, BulletY)
    if collision:
        BulletY = 320
        BulletState = "ready"
        Enemy_1_X = random.randint(0, 735)
        Enemy_1_Y = random.randint(15, 100)

    Enemy(Enemy_1_X, Enemy_1_Y)
    Player(PlayerX, PlayerY)
    pygame.display.update()
