'''
This module contains the underlying logic for Conway's Game of Life

Author: Tom Easterbrook
'''

import random


#This function generates a grid of cells in random states
def generate_grid(columns, rows):
    return [[random.randint(0,1)for x in range(columns)] for y in range(rows)]

#evolves the grid by applying a Game of Life Principles
def evolve_grid(grid):
   for column in range(len(grid)):
       for row in range(len(grid[column])):
          neighbours = check_neighbours(grid,column,row)
          if grid[column][row] == 1:
              # Over and under population
              if neighbours<2 or neighbours>3:
                   grid[column][row] = 0
          else:
              # Creation of life
              if neighbours == 3:
                  grid[column][row]=1
   # Survival is default position if none of the above conditions are met


# Checks how many neighbours of a specified cell are currently alive
def check_neighbours(grid,start_column,start_row):
    count = 0
    #N
    try:
        if grid[start_column + 1][start_row] == 1:
            count += 1
    except:
        pass
    #S
    try:
        if grid[start_column - 1][start_row] == 1:
            count += 1
    except:
        pass
    #E
    try:
        if grid[start_column][start_row+1] == 1:
            count += 1
    except:
        pass
    #W
    try:
        if grid[start_column][start_row-1] == 1:
            count += 1
    except:
        pass
    #NE
    try:
        if grid[start_column+1][start_row + 1] == 1:
            count += 1
    except:
        pass
    #SW
    try:
        if grid[start_column-1][start_row - 1] == 1:
            count += 1
    except:
        pass
    #NW
    try:
        if grid[start_column+1][start_row - 1] == 1:
            count += 1
    except:
        pass
    #NE
    try:
        if grid[start_column-1][start_row + 1] == 1:
            count += 1
    except:
        pass

    return count