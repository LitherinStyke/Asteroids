import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time):
        self.position += (self.velocity * delta_time)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return

        angle = random.uniform(20, 50)
        angle_positive = self.velocity.rotate(angle)
        angle_negitive = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = angle_positive * 1.2

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = angle_negitive