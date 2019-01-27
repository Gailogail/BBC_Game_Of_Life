'''
This module contains the underlying logic for Conway's Game of Life

Author: Tom Easterbrook
'''

import random


#This function generates a grid of cells in random states
def generate_grid(columns, rows):
    return [[random.randint(0,1)for x in range(columns)] for y in range(rows)]

def evolve_grid(grid):
   for column in range(len(grid)):
       for row in range(len(grid[column])):
          neighbours = check_neighbours(grid,column,row)
          if grid[column][row] == 1:
               if neighbours<2 or neighbours>3:
                   grid[column][row] = 0
          else:
              if neighbours == 3:
                  grid[column][row]=1




def check_neighbours(grid,start_column,start_row):
    count = 0
    try:
        if grid[start_column + 1][start_row] == 1:
            count += 1
    except:
        pass

    try:
        if grid[start_column - 1][start_row] == 1:
            count += 1
    except:
        pass
    try:
        if grid[start_column][start_row+1] == 1:
            count += 1
    except:
        pass
    try:
        if grid[start_column][start_row-1] == 1:
            count += 1
    except:
        pass
    try:
        if grid[start_column+1][start_row + 1] == 1:
            count += 1
    except:
        pass
    try:
        if grid[start_column-1][start_row - 1] == 1:
            count += 1
    except:
        pass
    try:
        if grid[start_column+1][start_row - 1] == 1:
            count += 1
    except:
        pass
    try:
        if grid[start_column-1][start_row + 1] == 1:
            count += 1
    except:
        pass

    return count


print(generate_grid(2, 3))