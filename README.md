README
======
This project is meant to provide easy 2D collision detection and handling for circles.  
#### MyCircle Class:
This class holds a 2D numpy array for position, radius, color, 2D numpy array for velocity, and width.  The "mass" property is calculated and assumed to be proportional to the area of the circle (i.e. constant density).
##### Methods:
1. display(screen)
  * Input is a screen object from pygame.  It draws a circle on the pygame screen.
2. move(dtime, screen_width, screen_height).  
  * dtime is the time increment.  The screen dimensions are required since the "move" method calls "bouce", which bounces the circles off the edge of the screen elastically.
3. change_vel(new_vel).  
  * Input is an numpy 2D array that holdes the desired velocity.  This method updates the circles velocity.
4. bounce(screen_width, screen_height).  
  * This method updates the velocity of the circles based on collisions with the edge of the screen.

#### "pycollide" Module:
Holds a variety of useful functions related to collisions
1. collide_circ(circle1, circle2).  
  * Input objects of MyCircle class.  This function returns the amount of overlap squared between two circles.  Specifically, it is the distance between the centers squared minus the sum of the radii squared.  If this quantity is negative it means there is overlap between the circles.
2. collision_direction(circle1, circle2).  
  * Input objects of MyCircle class.  This finds a unit vector pointed in the direction of the collision.  This is the direction that requires a velocity update.
3. circ_collision(circle1, circle2).  
  * Input objects of MyCircle class.  This function updates velocities of circles based on an elastic collision between two circles.  It accomplishes this by projecting velocities in the collision direction, updating them with elastic collision physics, and then converting back to original velocity vector positions.
4. overlap_move(circle1, circle2, screen_width, screen_height).  
  * Input objects of MyCircle class and screen dimensions.  This moves circles that are overlapping in the direction of their post-collision velocities until they no longer overlap.  The function incrementally updates the positions until there is no longer overlap.
