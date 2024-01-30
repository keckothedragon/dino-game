import pygame
from random import choice, randint
from utils.base_object import BaseObject
from utils.movement import Movement


class Cactus(BaseObject):
    SIZES = [
        (50, 50),
        (50, 30),
        (75, 75)
    ]

    def __init__(self, x: int, y: int, game_display: pygame.surface.Surface, speed: int):
        size = choice(Cactus.SIZES)
        super().__init__(x, y, *size, game_display, Movement(-speed, 0), False)
    
    def update(self):
        self.x += self.movement.delta_x
        self.y += self.movement.delta_y
        if self.x + self.width < 0:
            self.reset()
    
    def reset(self):
        super().reset()
        size = choice(Cactus.SIZES)
        self.width, self.height = size
        self.x += randint(100, 500)
