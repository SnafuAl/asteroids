# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():

    # Initialise PyGame
    pygame.init()

    # Set up screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up clock
    clock = pygame.time.Clock()
    dt = 0 # delta tiem

    # Game loop
    while True:
        # allow exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill("black")
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
