import os
import pygame
import gamestate
import tileclass


class Player:
    game_state = None

    def __init__(self, x, y, scale):
        self.scale = scale
        self.dt = 60
        self.x = x
        self.y = y
        self.player_dx = 0
        self.player_dy = 0
        self.player_max_dy = 0.25 * scale
        self.image = pygame.image.load(os.path.join("images", "theamongus.png"))
        self.image = pygame.transform.scale(self.image, (scale//2, scale//2))
        self.hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.movable = True

    def update(self, dt):
        self.dt = dt
        if self.movable:
            self.movement()

    def movement(self):
        keys = pygame.key.get_pressed()
        self.player_dx = (keys[pygame.K_d] - keys[pygame.K_a]) * 0.16 * self.scale
        self.player_dy += (0.05 * self.scale)
        self.player_dy = min(self.player_dy, self.player_max_dy)
        self.hit_box.move_ip(self.player_dx, self.player_dy)
        obj_list = Player.game_state.object_list
        static_obj_list = Player.game_state.static_object_list

        for i in range(len(static_obj_list)):
            if static_obj_list[i].__class__ == tileclass.Tile:
                if self.hit_box.colliderect(static_obj_list[i].hit_box):
                    blocked = False
                    if self.hit_box.midleft[0] <= static_obj_list[i].hit_box.right and static_obj_list[i].hit_box.\
                            bottom >= self.hit_box.midleft[1] >= static_obj_list[i].hit_box.top and self.hit_box.left \
                            >= (static_obj_list[i].hit_box.center[0] + static_obj_list[i].hit_box.right*2)//3:
                        self.player_dx = max(0, self.player_dx)
                        self.hit_box.left = static_obj_list[i].hit_box.right
                        blocked = True

                    if self.hit_box.midright[0] >= static_obj_list[i].hit_box.left and static_obj_list[i].hit_box.\
                            bottom >= self.hit_box.midright[1] >= static_obj_list[i].hit_box.top and self.hit_box.right\
                            <= (static_obj_list[i].hit_box.center[0] + static_obj_list[i].hit_box.left*2)//3:
                        self.player_dx = min(0, self.player_dx)
                        self.hit_box.right = static_obj_list[i].hit_box.left
                        blocked = True

                    if static_obj_list[i].hit_box.center[1] <= self.hit_box.top <= static_obj_list[i].hit_box.bottom \
                            and not blocked:
                        self.player_dy = max(self.player_dy, 0)
                        self.hit_box.top = static_obj_list[i].hit_box.bottom+1

                    if static_obj_list[i].hit_box.center[1] >= self.hit_box.bottom >= static_obj_list[i].hit_box.top \
                            and not blocked:
                        self.player_dy = 0
                        self.hit_box.bottom = static_obj_list[i].hit_box.top+1
                        if keys[pygame.K_SPACE]:
                            self.player_dy = -0.5 * self.scale
        if self.hit_box.bottom > Player.game_state.screen.get_height():
            self.player_dy = 0
            self.hit_box.bottom = 50

        self.x = self.hit_box.x
        self.y = self.hit_box.y
