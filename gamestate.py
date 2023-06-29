import sys
import pygame


class GameState:
    def __init__(self):
        self.state = "main_menu"

    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def stage(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def state_manager(self):
        if self.state == "main_menu":
            self.main_menu()
        elif self.state == "stage":
            self.stage()
