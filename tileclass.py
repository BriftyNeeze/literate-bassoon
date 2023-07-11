import os
import pygame


class Tile:
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

    def interact_y(self, player):
        if player.rect.colliderect(self.rect):
            if player.player_dy < 0:
                player.rect.top = self.rect.bottom
                player.player_dy = 0
            if player.player_dy > 0:
                player.rect.bottom = self.rect.top
                player.can_jump = True
                player.player_dy = 0

    def interact_x(self, player):
        if player.rect.colliderect(self.rect):
            if player.player_dx < 0:
                player.rect.left = self.rect.right
            if player.player_dx > 0:
                player.rect.right = self.rect.left


class SemiSolid(Tile):
    def __init__(self, x, y, width, height, scale):
        super().__init__(x, y, width, height, scale)
        self.height = 0.2

    def interact_y(self, player):
        if player.rect.colliderect(self.rect):
            if player.player_dy > 0:
                player.rect.bottom = self.rect.top
                player.can_jump = True
                player.player_dy = 0

    def interact_x(self, player):
        pass
