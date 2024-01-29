import pygame
import numpy as np
import constants
from utils.base_object import BaseObject
from utils.movement import Movement
from objects.dino import Dino

# init stuff
pygame.init()
game_display = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dino")
clock = pygame.time.Clock()

player = Dino(constants.PLAYER_X, constants.PLAYER_Y, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT, game_display,
              constants.PLAYER_JUMP_HEIGHT, pygame.image.load(constants.PLAYER_SPRITE_PATH))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.jump()
        if event.type == pygame.QUIT:
            running = False
    
    BaseObject.update_all()

    game_display.fill((0x00, 0xb2, 0x59)) # mechtech green

    BaseObject.draw_all()

    pygame.display.update()
    clock.tick(constants.FPS)