import pygame
import random
import math
from pygame import mixer

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

# Enemy

Enemy_1_Image = []
Enemy_1_X = []
Enemy_1_Y = []
Enemy_1_Xchange = []
Enemy_1_Ychange = []
num_of_enemies = 10

for i in range(num_of_enemies):
    Enemy_1_Image.append(pygame.image.load("EnemyAlien.png"))
    Enemy_1_X.append(random.randint(0, 735))
    Enemy_1_Y.append(random.randint(15, 100))
    Enemy_1_Xchange.append(0.1)
    Enemy_1_Ychange.append(25)

# Bullet

BulletImage = pygame.image.load("missile.png")
BulletX = 0
BulletY = 320
BulletXchange = 0
BulletYchange = .5
BulletState = "ready"

# Score System

score_value = 0
font = pygame.font.Font("Pixellettersfull-BnJ5.ttf", 40)

scoreX = 10
scoreY = 10

# Background

background = pygame.image.load("SpaceBackground.jpeg")

# Background Music

mixer.music.load("ravagers.mp3")
mixer.music.play(-1)


def Show_Score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 0, 255))
    screen.blit(score, (x, y))


def Player(x, y):
    screen.blit(PlayerImage, (x, y))


def Enemy(x, y, i):
    screen.blit(Enemy_1_Image[i], (x, y))


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
                    Bullet_Sound = mixer.Sound("TM88 Laser Shot.wav")
                    Bullet_Sound.play()
                    BulletX = PlayerX
                    Fire_Bullet(BulletX, BulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Xchange = 0

    # Enemy Movement

    for i in range(num_of_enemies):

        Enemy_1_X[i] += Enemy_1_Xchange[i]

        if Enemy_1_X[i] <= 0:
            Enemy_1_Xchange[i] = .1
            Enemy_1_Y[i] += Enemy_1_Ychange[i]
        elif Enemy_1_X[i] >= 736:
            Enemy_1_Xchange[i] = -.1
            Enemy_1_Y[i] += Enemy_1_Ychange[i]
        # Collision Detection
        collision = isCollision(Enemy_1_X[i], BulletX, Enemy_1_Y[i], BulletY)
        if collision:
            explosionSound = mixer.Sound("Invincible Explosion 1.wav")
            explosionSound.play()
            BulletY = 320
            BulletState = "ready"
            Enemy_1_X[i] = random.randint(0, 735)
            Enemy_1_Y[i] = random.randint(15, 100)
            score_value += 1
        Enemy(Enemy_1_X[i], Enemy_1_Y[i], i)

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

    Player(PlayerX, PlayerY)
    Show_Score(scoreX, scoreY)
    pygame.display.update()
