import os
import pygame
import buttonclass
import gamestate
import player
import stageloader


class ItemSelect:
    item_selected = None
    image_dict = {"block": pygame.image.load(os.path.join("images", "tileimg.jpeg"))}

    def __init__(self):
        pass

    @staticmethod
    def update():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        level_scale = stageloader.LevelLoader.level_scale

        grid_x = mouse_x // level_scale
        grid_y = mouse_y // level_scale
        grid = stageloader.LevelLoader.current_level
        if grid_x < 0 or grid_x >= len(grid[0]) or grid_y < 0 or grid_y >= len(grid):
            return
        state = pygame.mouse.get_pressed(num_buttons=3)[0]
        if not grid[grid_y][grid_x]:
            item = ItemSelect.item_selected
            display_image = ItemSelect.image_dict[item]
            display_image = pygame.transform.scale(display_image, (level_scale, level_scale))
            display_image.set_alpha(128)
            gamestate.GameState.scr.blit(display_image, (grid_x * level_scale, grid_y * level_scale))

            if state == 1:
                print("a")
