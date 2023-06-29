import pygame
import gamestate


def main():
    # Initialize
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    screen.fill((101, 238, 247))
    pygame.display.update()
    game_state = gamestate.GameState()

    # Title
    pygame.display.set_caption("Game")

    # Game Loop
    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(60)
        screen.fill((101, 238, 247))
        game_state.state_manager()

    pygame.quit()


if __name__ == '__main__':
    main()
