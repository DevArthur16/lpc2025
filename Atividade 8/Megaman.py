import pygame.sprite
from constants import *

def get_image(sheet, frame, width, height, scale, colour):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colour)

    return image

class Megaman(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet, sprite_width, sprite_height, sprite_quantity, sprite_scale):
        super().__init__()

        self.direction = DIRECTION_RIGHT

        sprite_sheet_image = pygame.image.load(sprite_sheet).convert_alpha()

        self.sprites = []

        for frame_index in range(sprite_quantity):
            self.sprites.append(get_image(sprite_sheet_image, frame_index, sprite_width, sprite_height, sprite_scale, COLOR_WHITE))

        self.index = 0
        self.image = self.sprites[self.index]

        self.rect = self.image.get_rect()

        # self.rect.topleft = SPRITE_START_COORD

        self.animate = False

    def update(self):
        if self.animate:
            self.index = self.index + 0.05
            if self.index >= len(self.sprites):
                self.index = 0
                self.animate = False
            self.image = self.sprites[int(self.index)]

            self.move(1, 0)

    def move(self, d_x, d_y):
        if self.direction == DIRECTION_RIGHT:
            self.rect.x += d_x
            self.rect.y += d_y

        if self.direction == DIRECTION_LEFT:
            self.rect.x -= d_x
            self.rect.y -= d_y

        if self.rect.x >= (SCREEN_WIDTH - 24) and self.direction == DIRECTION_RIGHT:
            self.rect.x = 0

        if self.rect.x < 24 and self.direction == DIRECTION_LEFT:
            self.rect.x = SCREEN_WIDTH


    def walk(self, direction):
        self.attack(direction)


    def jump(self, direction):
        self.attack(direction)


    def shoot(self, direction):
        self.attack(direction)


    def attack(self, direction):
        self.animate = True
        self.direction = direction