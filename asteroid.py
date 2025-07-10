import pygame 
import random
import math
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius): 
        super().__init__(x, y, radius)
        # Generate and store lumpy outline points (relative to center)
        self.num_points = 12
        angle_step = 360 / self.num_points
        self.outline = []
        for i in range(self.num_points):
            angle = math.radians(i * angle_step)
            perturbed_radius = self.radius + random.uniform(-self.radius * 0.3, self.radius * 0.3)
            x_off = perturbed_radius * math.cos(angle)
            y_off = perturbed_radius * math.sin(angle)
            self.outline.append((x_off, y_off))

    def draw(self, screen):
        # Calculate absolute points from relative outline
        points = [(self.position.x + x_off, self.position.y + y_off) for (x_off, y_off) in self.outline]
        pygame.draw.polygon(screen, "white", points, 2)

    def update(self, dt): 
        self.position += (self.velocity * dt)

    def split(self): 
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b