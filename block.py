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
        self.rect = pygame.rect.Rect(self.x, self.y, 30, 10)
        self.status = 2

    def draw(self, screen):
        if self.status > 0:
            colors = [(255, 0, 0), (255, 0, 0), (0, 0, 255)]
            pygame.draw.rect(screen, colors[self.status], self.rect)
        else:
            self.rect = pygame.rect.Rect(-1000, -1000, 30, 10)

    def update(self, screen, ball):
        # self.check_collision(ball)
        self.draw(screen)