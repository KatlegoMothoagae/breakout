import pygame

# if rect1.colliderect(rect2):
#     overlap_area = rect1.clip(rect2)
#     if overlap_area.width < overlap_area.height:
#         if rect2.x > rect1.x:
#             print("Left side collision")
#         else:
#             print("Right side collision")
#     else:
#         if rect2.y > rect1.y:
#             print("Top side collision")
#         else:
#             print("Bottom side collision")


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.solid = pygame.image.load("assets/red_tile.png").convert_alpha()
        self.solid = pygame.transform.scale(self.solid, (30, 10))
        self.cracked = pygame.image.load("assets/cracked_red_tile.png").convert_alpha()
        self.cracked = pygame.transform.scale(self.cracked, (30, 10))
        self.rect = pygame.rect.Rect(self.x, self.y, 30, 10)
        # self.solid.get_rect()
        self.status = 2

    def draw(self, screen):
        if self.status > 0:
            tiles = [None, self.solid, self.cracked]
            screen.blit(tiles[self.status], (self.x, self.y))

            # screen.blit(self.solid, (self.x, self.y))
        else:
            self.rect = pygame.rect.Rect(-1000, -1000, 30, 10)

    def update(self, screen, ball):
        # self.check_collision(ball)
        self.draw(screen)