"""
An implementation of Conway's Game of Life for the BBC technical test using Python 3 and Pygame

Author: Tom Easterbrook
Assumptions:

1. Although the algorithm can run on as much data as memory well allow I have created a 50x50
sample to show the algorithms operation

2. It is assumed that any cells outside this sample are dead

This file is the main entry point to the program and controls the application interface

"""

import logic
import pygame

# Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# This sets the WIDTH and HEIGHT of each cell
CELL_W = 10
CELL_H = 10

# This sets the gap between each cell
GAP = 10

# Generate  grid
grid = logic.generate_grid(25, 25)

# Start pygame
pygame.init()

# Load font
font = pygame.font.SysFont("Arial", 15)

# Set the HEIGHT, WIDTH and title of the screen
WINDOW_SIZE = [600, 600]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Conway's Game of Life")

closed = False
evolve_count = 1

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not closed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
            # Uncomment to enable evolution by evolution debugging
            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                grid = logic.evolve_grid(grid)
                evolve_count += 1
            '''

            # Set the screen background
        # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            color = WHITE
            if grid[row][column] == logic.CellState.ALIVE:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(GAP + CELL_W) * column + GAP + 50,
                              (GAP + CELL_H) * row + GAP + 50,
                              CELL_W,
                              CELL_H])

    # Render labels
    title_label = font.render("Conway's Game of Life!", 1, (255, 255, 0))
    screen.blit(title_label, (250, 25))
    evolve_label = font.render(" Evolution # " + str(evolve_count), 1, (255, 255, 0))
    screen.blit(evolve_label, (250, 560))

    # Limit to 1 evolution per second
    clock.tick(1)

    # update the screen
    pygame.display.flip()

    # Evolve grid
    grid = logic.evolve_grid(grid)
    evolve_count += 1

pygame.quit()
