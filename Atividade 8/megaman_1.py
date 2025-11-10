import pygame
from pygame.locals import *
from Bullet import Bullet
from Megaman import Megaman
from constants import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

all_sprites_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

sprite_walking_right = Megaman(MEGAMAN_WALKING_RIGHT_SPRITE_SHEET, MEGAMAN_WALKING_RIGHT_SPRITE_WIDTH, MEGAMAN_WALKING_RIGHT_SPRITE_HEIGHT, MEGAMAN_WALKING_RIGHT_SPRITE_SHEET_SIZE, 2)
sprite_shooting_right = Megaman(MEGAMAN_SHOOTING_RIGHT_SPRITE_SHEET, MEGAMAN_SHOOTING_RIGHT_SPRITE_WIDTH, MEGAMAN_SHOOTING_RIGHT_SPRITE_HEIGHT, MEGAMAN_SHOOTING_RIGHT_SPRITE_SHEET_SIZE, 2)
sprite_jumping_right = Megaman(MEGAMAN_JUMPING_RIGHT_SPRITE_SHEET, MEGAMAN_JUMPING_RIGHT_SPRITE_WIDTH, MEGAMAN_JUMPING_RIGHT_SPRITE_HEIGHT, MEGAMAN_JUMPING_RIGHT_SPRITE_SHEET_SIZE, 2)

sprite_walking_left = Megaman(MEGAMAN_WALKING_LEFT_SPRITE_SHEET, MEGAMAN_WALKING_LEFT_SPRITE_WIDTH, MEGAMAN_WALKING_LEFT_SPRITE_HEIGHT, MEGAMAN_WALKING_LEFT_SPRITE_SHEET_SIZE, 2)
sprite_shooting_left = Megaman(MEGAMAN_SHOOTING_LEFT_SPRITE_SHEET, MEGAMAN_SHOOTING_LEFT_SPRITE_WIDTH, MEGAMAN_SHOOTING_LEFT_SPRITE_HEIGHT, MEGAMAN_SHOOTING_LEFT_SPRITE_SHEET_SIZE, 2)
sprite_jumping_left = Megaman(MEGAMAN_JUMPING_LEFT_SPRITE_SHEET, MEGAMAN_JUMPING_LEFT_SPRITE_WIDTH, MEGAMAN_JUMPING_LEFT_SPRITE_HEIGHT, MEGAMAN_JUMPING_LEFT_SPRITE_SHEET_SIZE, 2)

is_running = True

direction = DIRECTION_RIGHT

while is_running:
    screen.fill(COLOR_BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
            all_sprites_group.empty()
            all_sprites_group.add(sprite_walking_right)
            sprite_walking_right.walk(DIRECTION_RIGHT)
            direction = DIRECTION_RIGHT

        if event.type == pygame.KEYDOWN and event.key == K_LEFT:
            all_sprites_group.empty()
            all_sprites_group.add(sprite_walking_left)
            sprite_walking_left.walk(DIRECTION_LEFT)
            direction = DIRECTION_LEFT

        if event.type == pygame.KEYDOWN and event.key == K_SPACE:
            all_sprites_group.empty()
            if direction == DIRECTION_RIGHT:
                all_sprites_group.add(sprite_jumping_right)
                sprite_jumping_right.jump(DIRECTION_RIGHT)
            if direction == DIRECTION_LEFT:
                all_sprites_group.add(sprite_jumping_left)
                sprite_jumping_left.jump(DIRECTION_LEFT)

        if event.type == pygame.KEYDOWN and event.key == K_RETURN:
            all_sprites_group.empty()
            if direction == DIRECTION_RIGHT:
                all_sprites_group.add(sprite_shooting_right)
                sprite_shooting_right.shoot(DIRECTION_RIGHT)
                bullet_x = sprite_shooting_right.rect.right
                bullet_y = sprite_shooting_right.rect.centery
                bullet = Bullet(bullet_x, bullet_y, DIRECTION_RIGHT)
            else:
                all_sprites_group.add(sprite_shooting_left)
                sprite_shooting_left.shoot(DIRECTION_LEFT)
                bullet_x = sprite_shooting_left.rect.left
                bullet_y = sprite_shooting_left.rect.centery
                bullet = Bullet(bullet_x, bullet_y, DIRECTION_LEFT)
            bullet_group.add(bullet)

    all_sprites_group.draw(screen)
    all_sprites_group.update()
    bullet_group.update()
    bullet_group.draw(screen)    # Draw bullets over sprites

    pygame.display.flip()

pygame.quit()