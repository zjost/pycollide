import math, pygame
import numpy as np

# Build a circle class
class MyCircle:

    def __init__ (self, pos, radius, color = (255, 0, 0),
                  vel = np.array([0,0]),width=0):
        self.pos = pos
        self.radius = radius
        self.color = color
        self.width = width
        self.vel = vel
        # Make mass proportional to area
        self.mass = math.pi*radius**2

    # A method for displaying a circle.
    # Note:  "screen" variable is from "pygame.display.set_mode(screen_size)"
    def display(self, screen):
        rx, ry = int(self.pos[0]), int(self.pos[1])
        pygame.draw.circle(screen, self.color, (rx, ry), self.radius, self.width)
    
    # A method for moving the circle
    def move(self, dtime, screen_width, screen_height):
        self.pos = self.pos + self.vel * dtime
        self.bounce(screen_width, screen_height)

    # A method for changing the velocity of a circle
    def change_vel(self, new_vel):
        self.vel = new_vel

    # A method for bouncing the balls elastically off the screen edge
    def bounce(self, screen_width, screen_height):
        if self.pos[0] <= self.radius:
            self.pos[0] = 2*self.radius - self.pos[0]
            self.vel[0] = -self.vel[0]
        elif self.pos[0] >= screen_width - self.radius:
            self.pos[0] = 2*(screen_width - self.radius) - self.pos[0]
            self.vel[0] = -self.vel[0]
        elif  self.pos[1] <= self.radius:
            self.pos[1] = 2*self.radius - self.pos[1]
            self.vel[1] = -self.vel[1]
        elif self.pos[1] >= screen_height - self.radius:
            self.pos[1] = 2*(screen_height - self.radius) - self.pos[1]
            self.vel[1] = -self.vel[1]


