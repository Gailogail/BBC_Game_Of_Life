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
CELL_W = 20
CELL_H = 20

# This sets the gap between each cell
GAP = 5

# Generate  grid
grid = l.generate_grid(10,10)

# start pygame
pygame.init()

# Set the HEIGHT, WIDTH and title of the screen
WINDOW_SIZE = [255, 255]
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