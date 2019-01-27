'''
This module contains the underlying logic for Conway's Game of Life

Author: Tom Easterbrook
'''

import random


#This function generates a grid of cells in random states
def generate_grid(columns, rows):
    return [[random.randint(0,1)for x in range(columns)] for y in range(rows)]

def evolve_grid(grid):
    pass
def check_neighbours(grid,start_x,start_y):
    pass


print(generate_grid(2, 3))