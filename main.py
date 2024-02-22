import pygame
from Player import Player
from ball import Ball
from level import Level
from block import Block
from helpers import *
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((600, 600))
char = Player(600 // 2 - 15, 600 - 25, 40)
ball = Ball(300, 300)
block = []
for x in range(20):
    for y in range(30):
        block.append(Block(x*30, y*10))
level = Level(char, ball, block)
sprite_sheet((100,50), "Paddle_Parts.png",)
while True:
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    level.update(window)
    pygame.display.update()
    clock.tick(60)