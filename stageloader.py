from collections import defaultdict
import pygame
import buttonclass
import gameinformation
import player
import gamestate
import tileclass


# level = [
#     "........................",
#     "........................",
#     "........................",
#     "........................",
#     "........................",
#     "........................",
#     "........................",
#     "........x.....xxxxxxxxxx",
#     "........x...............",
#     "xxxxxxxxxxx.............",
#     [("regular_tile_one", 100)]
# ]

level = [
    "............",
    "............",
    "yyyy....xxxx",
    "............",
    "xxxxx..xxxxx",
    [("regular_tile_one", 100, 1, 1)]  # object, count, grid width, grid height
]


class LevelLoader:
    def __init__(self):
        self.level_width = 50
        self.level_height = 50
        self.level_scale = 1
        self.current_level = []
        self.tile_count = defaultdict(int)

    def create_level(self):
        object_list = list()
        static_object_list = list()
        self.current_level = []

        self.level_scale = min(gameinformation.game_state.screen.get_height() // (len(level)-1) * 0.9, 
                               gameinformation.game_state.screen.get_width() // len(level[0]))
        self.level_width = self.level_scale * len(level[0])
        self.level_height = self.level_scale * (len(level)-1)
        self.level_scale = self.level_scale
        player.Player(50, 50, self.level_scale)

        for i in range(len(level)-1):
            self.current_level.append([])
            for j in range(len(level[i])):
                if level[i][j] == "x":
                    obj = tileclass.Tile(0 + j, 0 + i, 1, 1, self.level_scale)
                    static_object_list.append(obj)
                    self.current_level[i].append((obj, False))  # object, deletable
                elif level[i][j] == "y":
                    obj = tileclass.SemiSolid(0 + j, 0 + i, 1, 0.2, self.level_scale)
                    static_object_list.append(obj)
                    self.current_level[i].append((obj, False))  # object, deletable
                else:
                    self.current_level[i].append(None)

        for i in range(len(level[-1])):
            if level[-1][i][0] == "regular_tile_one":
                button = buttonclass.ItemButton(gameinformation.game_state.screen.get_width() // 2,
                                                gameinformation.game_state.screen.get_height() * 0.9, 50, 50,
                                                level[-1][i][0], level[-1][i][2], level[-1][i][3])
                object_list.append(button)
                self.tile_count[level[-1][i][0]] = level[-1][i][1]

        return object_list, static_object_list
