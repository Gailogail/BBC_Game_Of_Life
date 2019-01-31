'''
This module contains the underlying logic for Conway's Game of Life

Author: Tom Easterbrook
'''

import random


#  Generates a grid of cells in random states
def generate_grid(columns, rows):
    return [[random.randint(0,1)for x in range(columns)] for y in range(rows)]


# Generate a seeded glider pattern within the grade for testing purposes only
def generate_glider_grid():
    grid = [[0 for x in range(25)] for y in range(25)]

    grid[2][3]= 1
    grid[2][4] = 1
    grid[2][5] = 1

    grid[1][5] = 1

    grid[0][4] = 1

    return  grid
# Evolves the grid by applying a Game of Life Principles
def evolve_grid(grid):
   for row in range(len(grid)):
       for column in range(len(grid[row])):
          neighbours = check_neighbours(grid, row, column)
          if grid[row][column] == 1:
              # Over and under population
              if neighbours<2:
                   grid[row][column] = 0
              elif  neighbours > 3:
                  grid[row][column] = 0
          else:
              # Creation of life
              if neighbours == 3:
                  grid[row][column]=1

   # Survival is default position if none of the above conditions are met


# Checks how many neighbours of a specified cell are currently alive
def check_neighbours(grid, start_row, start_column):
    count = 0
    #N-S
    try:
        count += grid[start_row+1][start_column]
    except:
        pass
    try:
        count += grid[start_row-1][start_column]
    except:
        pass

    #W-E
    try:
        count += grid[start_row][start_column+1]
    except:
        pass
    try:
        count += grid[start_row][start_column -1]
    except:
        pass

    #Nw-Sw
    try:
        count += grid[start_row+1][start_column-1]
    except:
        pass
    try:
        count += grid[start_row-1][start_column-1]
    except:
        pass

     # NE-SE
    try:
        count += grid[start_row + 1][start_column + 1]
    except:
        pass
    try:
        count += grid[start_row - 1][start_column - 1]
    except:
        pass
    return count

