import os

import pygame
import buttonclass
import player


class ItemSelect:
    item_selected = None
    image_dict = {"block": pygame.image.load(os.path.join("images", "tileimg.jpeg"))}

    def __init__(self):
        pass

