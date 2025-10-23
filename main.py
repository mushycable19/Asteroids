# main.py
import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # --- SETUP CLOCK AND PLAYER ---
    clock = pygame.time.Clock()
    dt = 0

    # Spawn player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # --- GAME LOOP ---
    while True:
        # Handle input (exit on close)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw the game
        screen.fill((0, 0, 0))  # Black background
        player.draw(screen)     # Draw the player
        pygame.display.flip()   # Refresh the display

        # Limit to 60 FPS and get delta time
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
