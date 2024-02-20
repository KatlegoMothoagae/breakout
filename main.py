import pygame
from Player import Player
from ball import Ball
from level import Level
from block import Block
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((500, 500))
char = Player(500 // 2 - 15, 500 - 25, 40)
ball = Ball(100, 100)
block = Block(50, 50)
level = Level(char, ball, block)
while True:
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    level.update(window)
    pygame.display.update()
    clock.tick(60)