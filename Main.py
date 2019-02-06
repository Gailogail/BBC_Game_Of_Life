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

# This sets the WIDTH and HEIGHT of each cell
CELL_W = 10
CELL_H = 10

# This sets the gap between each cell
GAP = 1

# Generate  grid
grid = logic.generate_grid(25, 25)

# Start pygame
pygame.init()

# Load font
font = pygame.font.SysFont("Arial", 15)

# Define colours
BACKGROUND = pygame.color.Color("Black")
DEAD_CELL = pygame.color.Color("White")
ALIVE_CELL = pygame.color.Color("Green")
LABEL_TEXT = pygame.color.Color("Yellow")

# Set the HEIGHT, WIDTH and title of the screen
WINDOW_SIZE = [350, 350]
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
    screen.fill(BACKGROUND)

    # Draw the grid
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            color = DEAD_CELL
            if grid[row][column] == logic.CellState.ALIVE:
                color = ALIVE_CELL
            pygame.draw.rect(screen,
                             color,
                             [(GAP + CELL_W) * column + GAP + 35 ,
                              (GAP + CELL_H) * row + GAP + 35 ,
                              CELL_W,
                              CELL_H])

    # Render labels
    title_label = font.render("Conway's Game of Life!", 1, LABEL_TEXT)
    screen.blit(title_label, (125, 10))
    evolve_label = font.render(" Evolution # " + str(evolve_count), 1, LABEL_TEXT)
    screen.blit(evolve_label, (125, 320))

    # Limit to 1 evolution per second
    clock.tick(1)

    # update the screen
    pygame.display.flip()

    # Evolve grid
    grid = logic.evolve_grid(grid)
    evolve_count += 1

pygame.quit()
