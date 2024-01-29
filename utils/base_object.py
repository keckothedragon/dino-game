import pygame
import numpy as np
from utils.movement import Movement


class BaseObject:
    children = []
    def __init__(self, x: int, y: int, width: int, height: int, game_display: pygame.surface.Surface,
                 movement: Movement = Movement(), gravity: bool = False,
                 sprite: pygame.surface.Surface = None):
        self.x = x
        self.start_x = x
        self.y = y
        self.start_y = y
        self.width = width
        self.height = height
        self.movement = movement
        self.start_movement = Movement(movement.delta_x, movement.delta_y)
        self.game_display = game_display
        self.gravity = gravity
        self.sprite = sprite
        self.__class__.children.append(self)
    
    def set_movement(self, movement: Movement):
        self.movement = movement
    
    def update(self):
        if self.gravity is True:
            self.set_movement(Movement(0, self.movement.delta_y + 1))
        self.x += self.movement.delta_x
        self.y += self.movement.delta_y
        self.x = np.clip(self.x, 0, self.game_display.get_width() - self.width)
        self.y = np.clip(self.y, 0, self.game_display.get_height() - self.height)
    
    def draw(self):
        if self.sprite is not None:
            self.game_display.blit(self.sprite, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self.game_display, (0, 0, 0), (self.x, self.y, self.width, self.height))
    
    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.movement = self.start_movement
    
    @classmethod
    def update_all(cls):
        for child in cls.children:
            child.update()

    @classmethod
    def draw_all(cls):
        for child in cls.children:
            child.draw()


