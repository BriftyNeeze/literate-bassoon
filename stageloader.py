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
    ["block"]
]

# level = [
#     "............",
#     "............",
#     "xxxx....xxxx",
#     "............",
#     "xxxxx..xxxxx",
# ]


def create_level():

    object_list = list()
    static_object_list = list()
    scale = min(gamestate.GameState.scr.get_height() // len(level), gamestate.GameState.scr.get_width() // len(level[0]))
    plr = player.Player(50, 50, scale)
    object_list.append(plr)
    for i in range(len(level)-1):
        for j in range(len(level[0])):
            tile_button = buttonclass.TileButton(0 + j * scale, 0 + scale * i, 1, 1, scale)
            if level[i][j] == "x":
                obj = tileclass.Tile(0+j*scale, 0+scale*i, 1, 1, scale)
                static_object_list.append(obj)
                tile_button.filled = True

            object_list.append(tile_button)

    # fix position later
    for i in range(len(level[-1])):
        if level[-1][i] == "block":
            button = buttonclass.ItemButton(gamestate.GameState.scr.get_width()//2, gamestate.GameState.scr.get_height()*0.9, 50, 50, "block")
            object_list.append(button)

    return object_list, static_object_list

