import os
import pygame
import buttonclass
import gamestate
import player
import stageloader
import tileclass


class ItemSelect:
    game_state = None
    item_selected = None
    image_dict = {"regular_tile_one": pygame.image.load(os.path.join("images", "tileimg.jpeg"))}
    class_dict = {"regular_tile_one": (tileclass.Tile, 1, 1, "static")}
    button_pressed = False

    def __init__(self):
        pass

    @staticmethod
    def update():
        if stageloader.LevelLoader.tile_count[ItemSelect.item_selected] == 0:
            ItemSelect.item_selected = None
            return
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

            if state == 1 and not ItemSelect.button_pressed:
                ItemSelect.button_pressed = True
                stageloader.LevelLoader.tile_count[item] -= 1
                print(grid_x, grid_y)
                new_object = ItemSelect.class_dict[item][0](grid_x, grid_y, ItemSelect.class_dict[item][1], ItemSelect.
                                                            class_dict[item][2], stageloader.LevelLoader.level_scale)
                grid[grid_y][grid_x] = (new_object, True)
                if ItemSelect.class_dict[item][3] == "static":
                    ItemSelect.game_state.static_object_list.append(new_object)
                elif ItemSelect.class_dict[item][3] == "dynamic":
                    ItemSelect.game_state.object_list.append(new_object)
            elif state == 0:
                ItemSelect.button_pressed = False
