import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    delta_time = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    
    active_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(delta_time)
        for asteroid_index in asteroids:
            if asteroid_index.collision(active_player):
                print("Game over!")
                sys.exit()

            for shot_index in shots:
                if shot_index.collision(asteroid_index):

                    shot_index.kill()
                    asteroid_index.split()

        screen.fill("black")

        for index in drawable:
            index.draw(screen)

        pygame.display.flip()
        delta_time = clock.tick(60) / 1000

if __name__ == "__main__":
    main()