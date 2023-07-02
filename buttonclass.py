import os
import pygame
import stageloader
import itemselect
import gamestate


class Button:
    game_state = None

    def __init__(self, x, y, width, height):
        self.x = x - width // 2
        self.y = y - height // 2
        self.width = width
        self.height = height
        self.hit_box = pygame.Rect(self.x, self.y, width, height)
        self.image = pygame.image.load(os.path.join("images", "theamongus.png"))
        self.image = pygame.transform.scale(self.image, (width, height))
        self.let_go = True
        self.cooldown = 10
        self.curr_cooldown = 0
        self.dt = 60

    def update(self, dt):
        self.dt = dt
        pos = pygame.mouse.get_pos()
        # Clicking with the click then release to do action
        state = pygame.mouse.get_pressed(num_buttons=3)[0]
        if self.curr_cooldown != 0:
            self.curr_cooldown -= 1
        if self.hit_box.collidepoint(pos):
            if state == 1 and self.let_go and not self.curr_cooldown:
                self.action()
                self.curr_cooldown = self.cooldown
                self.let_go = False
            if state == 0:
                self.let_go = True

    def action(self):
        print("a")


class PlayButton(Button):
    def action(self):
        Button.game_state.object_list.clear()
        new_object_list, new_static_object_list = stageloader.LevelLoader.create_level()
        Button.game_state.object_list = new_object_list
        Button.game_state.static_object_list = new_static_object_list

        Button.game_state.state = "stage"


class ItemButton(Button):
    def __init__(self, x, y, width, height, block):
        super().__init__(x, y, width, height)
        self.block = block

    def action(self):
        itemselect.ItemSelect.item_selected = self.block



