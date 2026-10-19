from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
       pygame.draw.circle(screen, "white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        new1 = self.velocity.rotate(angle)
        new2 = self.velocity.rotate(-angle)
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        newas1 = Asteroid(self.position.x, self.position.y,smaller_radius )
        newas2 = Asteroid(self.position.x, self.position.y,smaller_radius )
        newas1.velocity = new1 * 1.2
        newas2.velocity = new2 * 1.2
