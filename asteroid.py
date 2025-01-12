import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return # This was a small asteroid

        # Creating split asteroid vectors
        random_angle = random.uniform(20, 50)
        vector_a = self.velocity.rotate(random_angle)
        vector_b = self.velocity.rotate(-random_angle)

        # Calculate split asteroids radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Creating split asteroids
        x = self.position.x
        y = self.position.y
        new_asteroid_a = Asteroid(x, y, new_radius)
        new_asteroid_b = Asteroid(x, y, new_radius)

        # Seting split asteroids direction and speeding them up
        new_asteroid_a.velocity = vector_a * 1.2
        new_asteroid_b.velocity = vector_b * 1.2

