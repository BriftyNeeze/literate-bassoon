import pygame
import buttonclass
import gameinformation
import gamestate
import itemselect
import player
import stageloader
import tileclass


def main():
    # Initialize
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    screen.fill((101, 238, 247))
    pygame.display.update()
    game_state = gamestate.GameState(screen)
    gameinformation.game_state = game_state
    buttonclass.Button.game_state = game_state
    player.Player.game_state = game_state
    tileclass.Tile.game_state = game_state
    itemselect.ItemSelect.game_state = game_state
    stageloader.LevelLoader.game_state = game_state

    button = buttonclass.PlayButton(screen.get_width()//2, screen.get_height()//2, 200, 60)
    game_state.object_list.append(button)
    del button
    # Title
    pygame.display.set_caption("Game")

    # Game Loop
    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(60)
        screen.fill((101, 238, 247))
        game_state.state_manager(dt)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
