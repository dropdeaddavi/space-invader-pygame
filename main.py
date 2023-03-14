import pygame

#initialize Pygame
pygame.init()

#Set Screen
screen = pygame.display.set_mode((800, 400))

#Window Display Settings

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#Player

PlayerImage = pygame.image.load("spacecraft.png")
PlayerX = 370
PlayerY = 320
Xchange = 0

def Player(x, y):

    screen.blit(PlayerImage, (x, y))

#Game Loop

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

    PlayerX += Xchange
    Player(PlayerX, PlayerY)
    pygame.display.update()
