"""
This module contains the underlying logic for Conway's Game of Life

Author: Tom Easterbrook
"""
import copy
import random


# A structure to represent the possible states of a cell
class CellState:
    DEAD = 0
    ALIVE = 1


#  Generates a grid of cells in random states
def generate_grid(rows, columns):
    grid = []
    for x in range(rows):
        row = []
        for y in range(columns):
            row.append(random.randint(CellState.DEAD, CellState.ALIVE))
        grid.append(row)
    return grid


# Generate a seeded glider pattern on the grid ( testing purposes only)
def generate_glider_grid(rows, columns):
    # Create blank grid
    grid = []
    for x in range(rows):
        row = []
        for y in range(columns):
            row.append(CellState.DEAD)
        grid.append(row)
    # Seed glider pattern
    grid[4][3] = CellState.ALIVE
    grid[4][4] = CellState.ALIVE
    grid[4][5] = CellState.ALIVE
    grid[3][5] = CellState.ALIVE
    grid[2][4] = CellState.ALIVE

    return grid


# Evolves the grid by applying a Game of Life Principles
def evolve_grid(current_grid):
    next_evolution = copy.deepcopy(current_grid)
    for row in range(len(current_grid)):
        for column in range(len(current_grid[row])):
            neighbours = check_neighbours(current_grid, row, column)
            if current_grid[row][column] == CellState.ALIVE:
                # Over and under population
                if neighbours < 2:
                    next_evolution[row][column] = CellState.DEAD
                elif neighbours > 3:
                    next_evolution[row][column] = CellState.DEAD
            else:
                # Creation of life
                if neighbours == 3:
                    next_evolution[row][column] = CellState.ALIVE
            # Survival is default position if none of the above conditions are met
    return next_evolution


# Checks how many neighbours of a specified cell are currently alive
# I appreciate this function is repetitive and could be improved
def check_neighbours(grid, start_row, start_column):
    count = 0
    # North
    try:
        count += grid[start_row + 1][start_column]
    except IndexError:
        pass
    # South
    try:
        if start_row > 0:
            count += grid[start_row - 1][start_column]
    except IndexError:
        pass
    # East
    try:
        count += grid[start_row][start_column + 1]
    except IndexError:
        pass
    # West
    try:
        if start_column > 0:
            count += grid[start_row][start_column - 1]
    except IndexError:
        pass
    # North East
    try:
        count += grid[start_row + 1][start_column + 1]
    except IndexError:
        pass
    # North West
    try:
        if start_column > 0:
            count += grid[start_row + 1][start_column - 1]
    except IndexError:
        pass
    # South East
    try:
        if start_row > 0:
            count += grid[start_row - 1][start_column + 1]
    except IndexError:
        pass
    # South West
    try:
        if (start_row > 0) & (start_column > 0):
            count += grid[start_row - 1][start_column - 1]
    except IndexError:
        pass
    return count
