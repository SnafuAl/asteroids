# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create player
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player =  Player(player_x, player_y)

    # Create asteroid field
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        # allow exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update updatables
        updatable.update(dt)

        # Check collisions with player
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return
            
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        # Drawing to screen
        screen.fill("black")
        for drawn in drawable:
            drawn.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
