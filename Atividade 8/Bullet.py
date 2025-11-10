import pygame
from constants import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.image.set_colorkey(COLOR_WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10 if direction == DIRECTION_RIGHT else -10

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()