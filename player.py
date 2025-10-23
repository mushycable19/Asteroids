# player.py
import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Player(CircleShape):
    def __init__(self, x, y):
        # Call parent constructor with x, y, and PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # initial facing direction

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    def draw(self, screen):
        # Draw the player as a white triangle outline
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        # Movement and rotation logic will go here later
        pass
