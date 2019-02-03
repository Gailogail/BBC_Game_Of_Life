'''
This module contains the underlying logic for Conway's Game of Life

Author: Tom Easterbrook
'''
import copy
import random


#  Generates a grid of cells in random states
def generate_grid(rows, columns):
    return [[random.randint(0,1)for x in range(columns)] for y in range(rows)]


# Generate a seeded glider pattern on the grid ( testing purposes only)
def generate_glider_grid():
    grid = [[0 for x in range(25)] for y in range(25)]

    grid[4][3]= 1
    grid[4][4] = 1
    grid[4][5] = 1

    grid[3][5] = 1

    grid[2][4] = 1

    return  grid


# Evolves the grid by applying a Game of Life Principles
def evolve_grid(current_grid):
    next_evolution = copy.deepcopy(current_grid)
    for row in range(len(current_grid)):
         for column in range(len(current_grid[row])):
            neighbours = check_neighbours(current_grid, row, column)
            if current_grid[row][column] == 1:
                # Over and under population
                if neighbours<2:
                    next_evolution[row][column] = 0
                elif  neighbours> 3:
                    next_evolution[row][column] = 0
            else:
                # Creation of life
                if neighbours == 3:
                    next_evolution[row][column]=1
            # Survival is default position if none of the above conditions are met
    return next_evolution


# Checks how many neighbours of a specified cell are currently alive
def check_neighbours(grid, start_row, start_column):
    count = 0
    # N
    try:
        count += grid[start_row+1][start_column]
    except IndexError:
        pass
    # S
    try:
        if start_row>0:
            count += grid[start_row-1][start_column]
    except IndexError:
        pass
    # E
    try:
        count += grid[start_row][start_column + 1]
    except IndexError:
        pass
    # W
    try:
        if start_column>0:
            count += grid[start_row][start_column - 1]
    except IndexError:
        pass
    # NE
    try:
        count += grid[start_row + 1][start_column +1]
    except IndexError:
        pass
    # NW
    try:
        if start_column>0:
            count += grid[start_row +1][start_column - 1]
    except IndexError:
        pass
    # SE
    try:
        if start_row>0:
            count += grid[start_row-1][start_column+1]
    except IndexError:
        pass
    # SW
    try:
        if (start_row>0) & (start_column>0):
            count += grid[start_row-1][start_column-1]
    except IndexError:
        pass
    return count
