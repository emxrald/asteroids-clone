import pygame

from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
from circleshape import CircleShape


class Player(CircleShape):
    """Player object controlled by user."""

    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a: pygame.Vector2 = self.position + forward * self.radius
        b: pygame.Vector2 = self.position - forward * self.radius - right
        c: pygame.Vector2 = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, pygame.Color("white"), self.triangle(), width=2)

    def rotate(self, dt: int) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: int) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)