import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    # --- WINDOW SETUP ---
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # --- CLOCK & DELTA TIME ---
    clock = pygame.time.Clock()
    dt = 0

    # --- CREATE GROUPS ---
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # --- ASSIGN GROUPS TO CLASSES ---
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)  # only updatable

    # --- CREATE GAME OBJECTS ---
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()  # spawns asteroids automatically

    # --- GAME LOOP ---
    while True:
        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # --- UPDATE PHASE ---
        updatable.update(dt)

        # --- COLLISION CHECK: player vs. all asteroids ---
        for ast in asteroids:
            if player.collides_with(ast):
                print("Game over!")
                return  # exits main() immediately


        # --- DRAW PHASE ---
        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # --- FRAME TIMING ---
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
