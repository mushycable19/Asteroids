# asteroid.py
import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw the asteroid as a hollow circle
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Move in a straight line at constant velocity
        self.position += self.velocity * dt