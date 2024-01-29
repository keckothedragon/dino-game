import pygame
from utils.base_object import BaseObject
from utils.movement import Movement


class Dino(BaseObject):
    def __init__(self, x: int, y: int, width: int, height: int, game_display: pygame.surface.Surface,
                 jump_height: int, sprite: pygame.surface.Surface = None):
        super().__init__(x, y, width, height, game_display, Movement(0, 0), True, sprite)
        self.jump_height = jump_height
    
    def jump(self):
        if self.y + self.height == self.game_display.get_height():
            self.set_movement(Movement(self.movement.delta_x, -self.jump_height))
