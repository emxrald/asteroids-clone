import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids..")

    # NUm of modules initialized
    ok, failed = pygame.init()
    print(f"Loaded {ok} pygame modules")
    print(f"Failed to load {failed} pygame modules")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    

    # Set sprite gorups for whole object classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    color_black = pygame.Color(0, 0, 0)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color_black)

        # Update objects
        updatable.update(dt)

        # Draw objects
        for item in drawable:
            item.draw(screen)

        # player.draw(screen)
        pygame.display.flip()

        # cap framerate to 60
        dt = game_clock.tick(60) / 1000  # convert dt to seconds


if __name__ == "__main__":
    main()
