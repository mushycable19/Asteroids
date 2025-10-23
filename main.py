import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    # --- WINDOW SETUP ---
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # --- SETUP CLOCK ---
    clock = pygame.time.Clock()
    dt = 0

    # --- CREATE GROUPS ---
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # --- ASSIGN GROUPS TO PLAYER CLASS ---
    Player.containers = (updatable, drawable)

    # --- CREATE PLAYER INSTANCE ---
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # --- GAME LOOP ---
    while True:
        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # --- UPDATE ALL OBJECTS ---
        updatable.update(dt)

        # --- DRAW ALL OBJECTS ---
        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # --- FRAME TIMING ---
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()