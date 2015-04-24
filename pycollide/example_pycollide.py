import os, sys, math, pygame, pygame.mixer
import random
import numpy as np
from pygame.locals import *
import pycollide as pc

# Defining some basic colors
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

# A list of colors
colors = [black, red, green, blue]

initial_vel = 40.

# Define the screen size
screen_size = screen_width, screen_height = 600, 400
             

def get_random_vel():
    new_angle = random.uniform(0, math.pi*2)
    new_x = math.cos(new_angle)
    new_y = math.sin(new_angle)
    new_vector = np.array([new_x, new_y])
    new_vector *= initial_vel
    return new_vector

# Setting the display and getting the surface object
screen = pygame.display.set_mode(screen_size)
# Getting the clock object
clock = pygame.time.Clock()
# Setting a title to the window
pygame.display.set_caption('Physics Play 4')

# Define number of circles and list object that will hold them
number_of_circles = 25
my_circles = []

# Loop to create circles

for n in range(number_of_circles):
    size = random.randint(10,20)
    x = random.randint(size, screen_width - size)
    y = random.randint(size, screen_height - size)
    pos = np.array([x, y])
    color = random.choice(colors)
    vel = get_random_vel()
    my_circles.append(pc.MyCircle(pos, size, color, vel))

direction_tick = 0.0

# Defining variables for fps and continued running
fps_limit = 60
run_me = True
while run_me:
    # Limit the framerate
    dtime_ms = clock.tick(fps_limit)
    dtime = dtime_ms/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_me = False

    # Clear the screen
    screen.lock()
    screen.fill(white)

    k = 0
    # Display my circles
    for i in range(0, len(my_circles)):
        for j in range(i+1, len(my_circles)):
            # Test if circles collide (separation distance is negative)
            circ1 = my_circles[i]
            circ2 = my_circles[j]
            if pc.collide_circ(circ1, circ2) < 0:
                pc.overlap_move(circ1,circ2, screen_width, screen_height)
                
    for my_circle in my_circles:
        my_circle.move(dtime, screen_width, screen_height)
        my_circle.display(screen)


    screen.unlock()    

    # Display everything in the screen
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()
