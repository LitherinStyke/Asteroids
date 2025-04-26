import pygame
import random
import math
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.points = self.generate_points()

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.points, 2)

    def generate_points(self):
        generated_points = []
        number_of_points = 10

        for i in range(number_of_points):
            distance = random.randrange(int(self.radius * 0.8), int(self.radius * 1.2))
            angle = 2 * math.pi * i / number_of_points
            x = self.position.x + distance * math.cos(angle)
            y = self.position.y + distance * math.sin(angle)
            generated_points.append(pygame.Vector2(x,y))

        return generated_points

    def update(self, delta_time):
        self.position += (self.velocity * delta_time)
        for point in self.points:
            point += (self.velocity * delta_time)

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