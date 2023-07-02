import pygame
import buttonclass
import player
import gamestate
import tileclass

level = [
    "........................",
    "........................",
    "........................",
    "........................",
    "........................",
    "........................",
    "........................",
    "..............xxxxxxxxxx",
    "........................",
    "xxxxxxxxxxx.............",
    [("block", 10)]
]

# level = [
#     "............",
#     "............",
#     "xxxx....xxxx",
#     "............",
#     "xxxxx..xxxxx",
# ]


class LevelLoader:
    level_width = 50
    level_height = 50
    level_scale = 1
    current_level = []

    def __init__(self):
        pass

    @staticmethod
    def create_level():
        object_list = list()
        static_object_list = list()
        LevelLoader.current_level = []

        scale = min(gamestate.GameState.scr.get_height() // (len(level)-1) * 0.9,
                    gamestate.GameState.scr.get_width() // len(level[0]))
        LevelLoader.level_width = scale * len(level[0])
        LevelLoader.level_height = scale * (len(level)-1)
        LevelLoader.level_scale = scale
        plr = player.Player(50, 50, scale)
        object_list.append(plr)
        for i in range(len(level)-1):
            LevelLoader.current_level.append([])
            for j in range(len(level[i])):
                if level[i][j] == "x":
                    obj = tileclass.Tile(0 + j * scale, 0 + scale * i, 1, 1, scale)
                    static_object_list.append(obj)
                    LevelLoader.current_level[i].append((obj, False))  # object, deletable
                else:
                    LevelLoader.current_level[i].append(None)

        for i in range(len(level[-1])):
            if level[-1][i][0] == "block":
                button = buttonclass.ItemButton(gamestate.GameState.scr.get_width() // 2,
                                                gamestate.GameState.scr.get_height() * 0.9, 50, 50, "block")
                object_list.append(button)

        return object_list, static_object_list
