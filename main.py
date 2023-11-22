# import functions from necessary modules
from random import randint
from math import trunc
from time import sleep
from copy import deepcopy
import os

generate_row = []
alphabet = [chr(i) for i in range(97, 123)]
grid_size = int(input("how big grid: "))
letter_to_number = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

final_grid = []
# create grid with only black squares
grid = [[ "⬛" for i in range(grid_size)] for j in range(grid_size)]

def display_grid(): # displays the final grid
    for i in final_grid:
        print("".join(i))

def run_conway(grid, final_grid):
    while True:
        os.system('cls')
        display_grid()

        for row_idx, row in enumerate(grid): # for every row in the grid
            for idx, cell in enumerate(row): # for every cell in the row
                alive_neighbors = 0

                for i in range(-1, 2): # both for loops are for deciding which surrounding value to check
                    for j in range(-1, 2):
                        if i == 0 and j == 0: # if its the centre value restarts the loop
                            continue
                        
                        neighbor_row = row_idx + i # current neighbour = current square + offset
                        neighbor_col = idx + j
                        try:                    
                            if grid[neighbor_row][neighbor_col] == "⬜": # if the neighbour square is white
                                alive_neighbors += 1 # add one to alive neighbours
                        except IndexError: # handles border errors 
                            pass
                if cell == "⬜" and (alive_neighbors < 2 or alive_neighbors > 3): # if current cell is white and there are less than 2 or more than 3 neighbours
                    final_grid[row_idx][idx] = "⬛" # current cell dies
                elif cell == "⬜" and (alive_neighbors == 2 or alive_neighbors == 3): # this code might be unnecessary but im too scared to change it and break everything
                    cell = "⬜"
                elif cell == "⬛" and alive_neighbors == 3: # if a dead cell as 3 alive neighbours, it becomes alive
                    final_grid[row_idx][idx] = "⬜"

        grid = deepcopy(final_grid) # set grid to final grid
        pc = input() # allows user to advance frame by frame


display_grid()

choice = input(f"write r to random gen a pattern (will add custom in future)").lower().strip()

if choice == "r":
    for i in range(randint(trunc((grid_size * grid_size) / 8), trunc((grid_size * grid_size) / 4))):
        row = randint(1,grid_size)
        col = randint(1,grid_size)
        grid[row - 1][col - 1] = "⬜"
    final_grid = deepcopy(grid)

    run_conway(grid, final_grid)
if choice == "e" and grid_size <= 26:
    new_row = ["  "]
    new_row_2 = ["  "]
    for i in range(grid_size):
        if i < 9:
            new_row_2.append("_ ")
            new_row.append(str(f'{i + 1} '))
        else:
            new_row_2.append(f'{str(i + 1)[0]} ')
            new_row.append(f'{str(i + 1)[1]} ')
    grid.insert(0, new_row)
    grid.insert(0, new_row_2)
    for idx, row in enumerate(grid):
        if idx == 0 or idx == 1:
            continue
        row.insert(0, alphabet[idx - 2])

    while True:
        final_grid = deepcopy(grid)
        display_grid()
        to_switch = input("Type save to stop editing.\nT the grid coordinate (letter first) here: ").lower().strip()
        if to_switch == "save":
            break
        coord_char = to_switch[0]
        try: coord_num = int(to_switch[1:])
        except ValueError: 
            print("Please enter a valid grid coordinate.") 
            continue
        if len(to_switch) < 2 or len(to_switch) > 3 or coord_char not in alphabet or coord_num > 26 or coord_num < 1:
            print("Please enter a valid grid coordinate.")
            continue
        row = letter_to_number[coord_char] + 1
        col = coord_num
        if grid[row][col] == "⬛":
            grid[row][col] = "⬜"
        else: grid[row][col] = "⬛"
else:
    pass

