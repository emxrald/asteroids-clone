import pygame

from constants import *


def main():
    print("Starting Asteroids..")

    # NUm of modules initialized
    ok, failed = pygame.init()
    print(f"Loaded {ok} pygame modules")
    print(f"Failed to load {failed} pygame modules")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    color_black = pygame.Color(0, 0, 0)

    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color_black)
        pygame.display.flip()

        # cap framerate to 60
        dt = game_clock.tick(60) / 1000  # convert dt to seconds


if __name__ == "__main__":
    main()
