import os
import pygame
import buttonclass
import gameinformation
import gamestate
import player
import stageloader
import tileclass


image_dict = {
    "regular_tile_one": pygame.image.load(os.path.join("images", "tileimg.jpeg")),
    "regular_semi_solid_one": pygame.image.load(os.path.join("images", "tileimg.jpeg"))
}

class_dict = {
    "regular_tile_one": (tileclass.Tile, "static"),
    "regular_semi_solid_one": (tileclass.Tile, "static")
}


class ItemSelect:
    def __init__(self):
        self.item_selected = None
        self.tile_width = 1
        self.tile_height = 1
        self.button_pressed = False

    def update(self):
        if gameinformation.level_loader.tile_count[self.item_selected] == 0:
            self.item_selected = None
            return
        mouse_x, mouse_y = pygame.mouse.get_pos()
        level_scale = gameinformation.level_loader.level_scale

        grid_x = mouse_x // level_scale
        grid_y = mouse_y // level_scale
        grid = gameinformation.level_loader.current_level
        if grid_x < 0 or grid_x >= len(grid[0]) or grid_y < 0 or grid_y >= len(grid):
            return
        state = pygame.mouse.get_pressed(num_buttons=3)[0]
        if not grid[grid_y][grid_x]:
            item = self.item_selected
            display_image = image_dict[item]
            display_image = pygame.transform.scale(display_image, (level_scale, level_scale))
            display_image.set_alpha(128)
            gameinformation.game_state.screen.blit(display_image, (grid_x * level_scale, grid_y * level_scale))

            if state == 1 and not self.button_pressed:
                self.button_pressed = True
                gameinformation.level_loader.tile_count[item] -= 1
                new_object = class_dict[item][0](grid_x, grid_y, self.tile_width, self.tile_height,
                                                 gameinformation.level_loader.level_scale)
                grid[grid_y][grid_x] = (new_object, True)
                if class_dict[item][1] == "static":
                    gameinformation.game_state.static_object_list.append(new_object)
                elif class_dict[item][1] == "dynamic":
                    gameinformation.game_state.object_list.append(new_object)
            elif state == 0:
                self.button_pressed = False
        elif self.item_selected == "delete" and grid[grid_y][grid_x][1]:
            pass
