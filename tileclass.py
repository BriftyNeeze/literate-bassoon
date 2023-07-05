import os
import pygame


class Tile:
    game_state = None

    def __init__(self, x, y, width, height, scale):
        self.x = x * scale
        self.y = y * scale
        self.width = width
        self.height = height
        self.scale = scale
        self.image = pygame.image.load(os.path.join("images", "tileimg.jpeg"))
        self.image = pygame.transform.scale(self.image, (self.width*scale, self.height*scale))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.dt = 60

    def update(self, dt):
        self.dt = dt
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

