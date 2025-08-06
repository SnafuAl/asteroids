# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player

def main():

    # Initialise PyGame
    pygame.init()

    # Set up screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up clock
    clock = pygame.time.Clock()
    dt = 0 # delta time

    # Set up sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Create player
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player =  Player(player_x, player_y)

    # Game loop
    while True:
        # allow exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update player
        updatable.update(dt)

        # Drawing to screen
        screen.fill("black")
        for drawn in drawable:
            drawn.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
