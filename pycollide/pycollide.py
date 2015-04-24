import numpy as np
import math, pygame

def collide_circ(circle1, circle2):
    # This function returns the amount of separation distance squared
    # If difference is negative, circles are too close
    x1, y1 = circle1.pos[0], circle1.pos[1]
    r1 = circle1.radius
    x2, y2 = circle2.pos[0], circle2.pos[1]
    r2 = circle2.radius
    dist_sqr = (y2-y1)**2+(x2-x1)**2
    return (dist_sqr - (r1+r2)**2)

def collision_direction(circle1, circle2):

    ''' Step 1: Create orthonormal basis vectors for collision direction '''
    # Get positional vectors
    r1 = circle1.pos
    r2 = circle2.pos
    # Get vector in collision direction
    x_hat_p = r2 - r1
    # Normalize vector
    x_hat = x_hat_p / math.sqrt(np.dot(x_hat_p, x_hat_p))

    # Find orthogonal vector using [0,1] and Gram-Schmidt
    y_vec = np.array([0,1])
    y_hat_p = y_vec - np.dot(x_hat,y_vec)*x_hat
    # Normalize vector
    y_hat = y_hat_p / math.sqrt(np.dot(y_hat_p, y_hat_p))

    return (x_hat, y_hat)

def circ_collision(circle1, circle2):

    coll_vec = collision_direction(circle1, circle2)
    
    # Separate out collision vector
    x_hat = coll_vec[0]
    y_hat = coll_vec[1]


    ''' Step 2: Project ball velocity vectors onto new basis set '''
    # Get original velocity vectors
    v1 = circle1.vel
    v2 = circle2.vel
    # Project onto new basis
    v_1x = np.dot(v1, x_hat)
    v_1y = np.dot(v1, y_hat)
    v_2x = np.dot(v2, x_hat)
    v_2y = np.dot(v2, y_hat)

    ''' Step 3: Update the velocities in these directions using
        elastic collision mechanics '''
    m1 = circle1.mass
    m2 = circle2.mass

    # Update velocities in collision direction
    # Note:  velocities in direction perpendicular to collision do not change
    v_1x_p = (v_1x*(m1-m2)+2*m2*v_2x)/(m1+m2)
    v_2x_p = (2*(v_1x)*m1+v_2x*(m2-m1))/(m1+m2)

    ''' Step 4: Create velocity vectors (in the collision direction basis) '''
    v1_p = np.array([v_1x_p, v_1y])
    v2_p = np.array([v_2x_p, v_2y])
    
    ''' Step 5: Convert these vectors back to original basis '''
    # Define conversion matrix
    A11 = np.dot(np.array([1, 0]), x_hat)
    A12 = np.dot(np.array([1, 0]), y_hat)
    A21 = np.dot(np.array([0, 1]), x_hat)
    A22 = np.dot(np.array([0, 1]), y_hat)
    A = np.array([[A11, A12], [A21, A22]])

    # Convert to original basis
    v1_new = np.dot(A, v1_p)
    v2_new = np.dot(A, v2_p)
    return (v1_new, v2_new)

def overlap_move(circle1, circle2,screen_width, screen_height):
    ''' This function moves overlapped circles in the direction
    of their new velocities until they no longer overlap '''
    vel_vec = circ_collision(circle1, circle2)
    move_1_dir = vel_vec[0]
    move_2_dir = vel_vec[1]
    circle1.change_vel(move_1_dir)
    circle2.change_vel(move_2_dir)
    overlap = collide_circ(circle1, circle2)
    while overlap < 0:
        # Change position of each circle by a small amount 
        circle1.move(.005,screen_width, screen_height)
        circle2.move(.005,screen_width, screen_height)
        overlap = collide_circ(circle1, circle2)

        
    
