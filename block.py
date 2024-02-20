import pygame

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(self.x, self.y, 30, 10)
        self.status = 2

    def draw(self, screen):
        if self.status > 0:
            colors = [(255, 0, 0), (255, 0, 0), (0, 0, 255)]
            pygame.draw.rect(screen, colors[self.status], self.rect)

    def check_collision(self, ball):
        if self.rect.colliderect(ball.rect):
            self.status -= 1
            ball.vel_y *= -1

    def update(self, screen, ball):
        self.check_collision(ball)
        self.draw(screen)