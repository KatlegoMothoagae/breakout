import pygame

class Ball:
    def __init__(self, x, y):
        self.vel_x = 4
        self.vel_y = 4
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(self.x, self.y, 10, 10)
        self.ball = pygame.image.load("assets/ball.png").convert_alpha()
        self.ball = pygame.transform.scale(self.ball, (10, 10))


    def change_dir(self, screen):
        if self.x >= screen.get_width():
            self.vel_x = -4

        elif self.x <= 0:
            self.vel_x = 4

        elif self.y >= screen.get_height():
            self.vel_y = -4

        elif self.y <= 0:
            self.vel_y = 4

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def update(self, screen):
        self.move()
        self.change_dir(screen)
        self.rect = pygame.rect.Rect(self.x, self.y, 5, 5)
        # pygame.draw.circle(screen,(0, 0, 0), (self.x, self.y), 5)
        screen.blit(self.ball, (self.x, self.y))
