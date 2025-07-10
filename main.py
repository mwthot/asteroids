import pygame
import sys
from player import * 
from circleshape import * 
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    dt = 0 

    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                return
        
        screen.fill("black")
        
        updatable.update(dt)
        
        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids: 
            if player.collides_with(asteroid): 
                print("Game over!")
                sys.exit()
            for shot in shots: 
                if asteroid.collides_with(shot):
                    obj.kill()
                    asteroid.kill()
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    


if __name__ == "__main__":
    main()
