import sys
import pygame
import buttonclass
import itemselect


class GameState:
    def __init__(self, screen):
        self.state = "main_menu"
        self.screen = screen
        self.object_list = []
        self.static_object_list = []
        self.player_group = pygame.sprite.Group()
        self.dt = 60

    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for obj in self.object_list:
            obj.update(self.dt)
            self.screen.blit(obj.image, (obj.x, obj.y))
        for obj in self.static_object_list:
            self.screen.blit(obj.image, (obj.x, obj.y))

    def stage(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.player_group.update(self.dt)
        self.player_group.draw(self.screen)
        for obj in self.object_list:
            obj.update(self.dt)
            self.screen.blit(obj.image, (obj.x, obj.y))
        for obj in self.static_object_list:
            self.screen.blit(obj.image, (obj.x, obj.y))

        if itemselect.ItemSelect.item_selected:
            itemselect.ItemSelect.update()

    def state_manager(self, dt):
        self.dt = dt
        if self.state == "main_menu":
            self.main_menu()
        elif self.state == "stage":
            self.stage()
