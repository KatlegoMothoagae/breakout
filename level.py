import pygame


class Level:
    def __init__(self, player, ball, blocks):
        self.player = player
        self.ball = ball
        self.blocks = blocks
    def check_collision(self):
        if self.ball.rect.colliderect(self.player.rect):
            self.ball.vel_y *= -1


        # elif self.ball.rect.colliderect(self.ball.rect):
        #     self.ball.vel_y *= -1

    def update(self, screen):
        self.check_collision()
        self.player.update(screen)
        self.ball.update(screen)
        self.blocks.update(screen, self.ball)
