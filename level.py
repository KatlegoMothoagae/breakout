import pygame


class Level:
    def __init__(self, player, ball, blocks):
        self.player = player
        self.ball = ball
        self.blocks = blocks
    def check_collision_player(self):
        if self.ball.rect.colliderect(self.player.rect):
            # if self.ball.rect.bottom <= self.player.rect.top:
                print("collision!")
                self.ball.vel_y = -4


        # elif self.ball.rect.colliderect(self.ball.rect):
        #     self.ball.vel_y *= -1
    def check_collision(self):
        for block in self.blocks:
            if block.rect.colliderect(self.ball.rect):
                """check which side the ball collides with the block left side 
                vel_x = - 2, right side vel_x = 2, top vel_y = 2, bottom vel_y = -2"""
                block.status -= 1
                # ball.vel_y *= -1
                if block.status >= 0:
                    self.ball.vel_y *= -1
                    overlap_area = block.rect.clip(self.ball.rect)
                    if overlap_area.width < overlap_area.height:
                        if self.ball.rect.x > block.rect.x:
                            self.ball.vel_x = 4
                        else:
                            self.ball.vel_x = -4
                    else:
                        if self.ball.rect.y > block.rect.y:
                            self.ball.vel_y = 4
                        else:
                            self.ball.vel_y = -4
                break

    def update_blocks(self, screen):
        for block in self.blocks:
            block.update(screen, self.ball)
    def update(self, screen):
        self.check_collision_player()
        self.check_collision()
        self.player.update(screen)
        self.ball.update(screen)
        self.update_blocks(screen)