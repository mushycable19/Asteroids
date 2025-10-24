# asteroid.py
import pygame
import random                          # <-- NEW
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    # --- NEW ---
    def split(self):
        # This asteroid is always destroyed
        self.kill()

        # Smallest size: nothing to spawn
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Choose a random split angle (deg) to branch left/right
        random_angle = random.uniform(20, 50)

        # New velocities (split to opposite sides)
        v1 = self.velocity.rotate(+random_angle) * 1.2
        v2 = self.velocity.rotate(-random_angle) * 1.2

        # New radius (one size smaller)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two new asteroids at the same position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = v2
