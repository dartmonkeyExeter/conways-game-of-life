from random import randint
from math import trunc
from time import sleep
import os



generate_row = []

what_to_do = {
    1: [-1, -1],
    2: [-1, 0],
    3: [-1, 1],
    4: [-1, 0],
    5: [1, 0],
    6: [-1, -1],
    7: [-1, 0],
    8: [-1, 1],
}


grid_size = int(input())


grid = [[ "⬛" for i in range(grid_size)] for j in range(grid_size)]
final_grid = grid

def display_grid():
    for i in final_grid:
        print("".join(i))

def run_conway():
    while True:
        os.system("cls")
        for row_idx, row in enumerate(grid):
            for idx, i in enumerate(row):
                if i == "⬜":
                    current_surronding = 1
                    dead_amount = 0
                    alive_amount = 0
                    while True:
                        if current_surronding == 9:
                            break
                        list_to_check = what_to_do[current_surronding]
                        try:
                            colour = grid[row_idx + list_to_check[0]][idx + list_to_check[1]]
                            if colour == "⬛":
                                dead_amount += 1
                            else:
                                alive_amount += 1
                        except IndexError:
                            pass
                        current_surronding += 1
                    if dead_amount < 2 or alive_amount > 3:
                        final_grid[row_idx][idx] = "⬛"
                elif i == "⬛":
                    current_surronding = 1
                    dead_amount = 0
                    alive_amount = 0
                    while True:
                        if current_surronding == 9:
                            break
                        list_to_check = what_to_do[current_surronding]
                        try:
                            colour = grid[row_idx + list_to_check[0]][idx + list_to_check[1]]
                            if colour == "⬛":
                                dead_amount += 1
                            else:
                                alive_amount += 1
                        except IndexError:
                            pass
                        current_surronding += 1
                    if alive_amount == 3:
                        final_grid[row_idx][idx] = "⬜"
        display_grid()
        sleep(0.5)


display_grid()

choice = input(f"would you like to randomly generate a pattern, load a pattern, or create a pattern? (r/l/c)").lower().strip()



if choice == "r":
    for i in range(randint(trunc((grid_size * grid_size) / 8), trunc((grid_size * grid_size) / 4))):
        row = randint(1,grid_size)
        col = randint(1,grid_size)
        grid[row - 1][col - 1] = "⬜"

final_grid = grid

run_conway()


