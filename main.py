from random import randint
from math import trunc
from time import sleep
from copy import deepcopy
import os

generate_row = []


grid_size = int(input())

final_grid = []
grid = [[ "⬛" for i in range(grid_size)] for j in range(grid_size)]

def display_grid():
    for i in final_grid:
        print("".join(i))

def run_conway(grid, final_grid):
    while True:
        display_grid()

        for row_idx, row in enumerate(grid):
            for idx, cell in enumerate(row):
                alive_neighbors = 0

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue

                        neighbor_row = row_idx + i
                        neighbor_col = idx + j
                        try:                    
                            if grid[neighbor_row][neighbor_col] == "⬜":
                                alive_neighbors += 1
                        except IndexError:
                            pass
                if cell == "⬜" and (alive_neighbors < 2 or alive_neighbors > 3):
                    final_grid[row_idx][idx] = "⬛"
                elif cell == "⬜" and (alive_neighbors == 2 or alive_neighbors == 3):
                    cell = "⬜"
                elif cell == "⬛" and alive_neighbors == 3:
                    final_grid[row_idx][idx] = "⬜"

        grid = deepcopy(final_grid)
        pc = input()


display_grid()

choice = input(f"write r to random gen a pattern (will add custom in future)").lower().strip()



if choice == "r":
    for i in range(randint(trunc((grid_size * grid_size) / 8), trunc((grid_size * grid_size) / 4))):
        row = randint(1,grid_size)
        col = randint(1,grid_size)
        grid[row - 1][col - 1] = "⬜"
else:
    pass

final_grid = deepcopy(grid)

run_conway(grid, final_grid)
