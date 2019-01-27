'''
An implementation of Conway's Game of Life for the BBC technical test using Python 3 and Pygame

Author: Tom Easterbrook
Assumptions:

This file is the main entry point to the program and controls the application interface
'''

import logic as l
import pygame

# Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# This sets the WIDTH and HEIGHT of each cell
CELL_W = 5
CELL_H = 5

# This sets the gap between each cell
GAP = 5

# Generate  grid
grid = l.generate_grid(100,100)

# start pygame
pygame.init()

# Set the HEIGHT, WIDTH and title of the screen
WINDOW_SIZE = [1000, 1000]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Conway's Game of Life")


closed = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not closed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
        # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            color = WHITE
            if grid[row][column] == 1:
                 color = GREEN
            pygame.draw.rect(screen,
                            color,
                            [(GAP + CELL_W) * column + GAP,
                            (GAP + CELL_H) * row + GAP,
                            CELL_W,
                            CELL_H])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
pygame.quit()