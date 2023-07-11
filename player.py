import os
import pygame
import gameinformation
import gamestate
import stageloader
import tileclass


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.dt = 60
        self.x = x
        self.y = y
        self.player_dx = 0
        self.player_dy = 0
        self.player_max_dy = 0.25 * scale
        self.image = pygame.image.load(os.path.join("images", "theamongus.png"))
        self.image = pygame.transform.scale(self.image, (scale//2, scale//2))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.movable = True
        self.can_jump = False
        pygame.sprite.Sprite.add(self, gameinformation.game_state.player_group)

    def update(self, dt):
        self.dt = dt
        if self.movable:
            self.movement()

    def movement(self):
        keys = pygame.key.get_pressed()
        self.player_dx = (keys[pygame.K_d] - keys[pygame.K_a]) * 0.16 * self.scale
        self.player_dy += (0.05 * self.scale)
        self.player_dy = min(self.player_dy, self.player_max_dy)
        # obj_list = gameinformation.game_state.object_list
        # static_obj_list = gameinformation.game_state.static_object_list
        level_grid = gameinformation.level_loader.current_level
        grid_x = self.x // self.scale
        grid_y = self.y // self.scale

        # check blocks in a 3x3 radius
        calculate_list = []
        for i in range(3):
            if grid_x + i - 1 >= len(level_grid[0]) or grid_x + i - 1 < 0:
                continue
            for j in range(3):
                if grid_y+j-1 >= len(level_grid) or grid_y+j-1 < 0:
                    continue
                if level_grid[grid_y+j-1][grid_x+i-1]:
                    calculate_list.append(level_grid[grid_y+j-1][grid_x+i-1])

        # vertical check
        self.rect.y += self.player_dy
        self.can_jump = False
        for obj in calculate_list:
            obj[0].interact_y(self)

        # horizontal check
        self.rect.x += self.player_dx
        for obj in calculate_list:
            obj[0].interact_x(self)

        if keys[pygame.K_SPACE] and self.can_jump:
            self.player_dy = -0.5 * self.scale

        if self.rect.bottom > gameinformation.game_state.screen.get_height():
            self.player_dy = 0
            self.rect.bottom = 50

        self.x = self.rect.x
        self.y = self.rect.y
