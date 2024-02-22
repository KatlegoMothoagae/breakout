import pygame
class Player:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.rect = pygame.rect.Rect(self.x, self.y, width, 10)
        self.player= pygame.image.load("assets/player.png").convert_alpha()
        self.player = pygame.transform.scale(self.player, (self.width, 10))

    def draw_player(self, screen):
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, 10)
        pygame.draw.rect(screen, (0, 0, 0), self.rect)

    def move_player(self, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if self.x + self.width < screen.get_width():
                self.x += 6
        elif keys[pygame.K_a]:
            if self.x > 0:
                self.x -= 6
    def update(self, screen):
        self.move_player(screen)
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, 10)

        screen.blit(self.player, (self.x, self.y))