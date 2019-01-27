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
CELL_W = 10
CELL_H = 10

# This sets the gap between each cell
GAP = 10

# Generate  grid
grid = l.generate_grid(25,25)

# start pygame
pygame.init()

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
                            [(GAP + CELL_W) * column + GAP+50,
                            (GAP + CELL_H) * row + GAP+50,
                            CELL_W,
                            CELL_H])
    font = pygame.font.SysFont("Arial", 15)

    # render labels
    title_label = font.render("Conway's Game of Life!", 1, (255, 255, 0))
    screen.blit(title_label, (250, 25))
    evolve_label = font.render(" Evolution # "+str(evolve_count), 1, (255, 255, 0))
    screen.blit(evolve_label, (250, 560))

    # Limit to 1 evolution per second
    clock.tick(1)

    # update the screen with what we've drawn.
    pygame.display.flip()
    l.evolve_grid(grid)
    evolve_count+=1

pygame.quit()