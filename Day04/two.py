#! /usr/bin/env python3

import numpy as np

# Function to calculate a cells diag neighbour pairs
def get_diag_neighbours(x,y):
    pair_1 = [[x - 1, y - 1], [x + 1, y + 1]]
    pair_2 = [[x - 1, y + 1], [x + 1, y - 1]]
    return(pair_1,pair_2)


# Function to establish if cell is on a boundary
def boundary_check(x,y,cell):
    x -= 1
    y -= 1
    if cell[0] in [0,y] or cell[1] in [0,x]:
        return True
    else:
        return False
    

# Function to look up neighbour pair values and return if they match MS or SM
def check_neighbours(neighbours):
    pair1_vals = []
    pair2_vals = []
    for cell in neighbours[0]:
        x = cell[0]
        y = cell[1]
        pair1_vals.append(str(new_grid[x,y]))
    for cell in neighbours[1]:
        x = cell[0]
        y = cell[1]
        pair2_vals.append(str(new_grid[x,y]))
    pair1_vals.sort()
    pair2_vals.sort()
    if pair1_vals == ["M","S"] and pair2_vals == ["M","S"]:
        return True
    else:
        return False


# Check dimensions of file
lines = 0
f = open("input.txt", "r")
for line in f.read().splitlines():
    line_length = len(line)
    lines += 1
f.close()

# Create 2D array with dummy first row
grid = np.zeros((1, line_length))

# Populate with real data
f = open("input.txt", "r")
for line in f.read().splitlines():
    as_list = list(line)
    grid = np.vstack([grid, as_list])

# Remove dummy first row
new_grid = np.delete(grid, 0, axis=0)

# Find the A's
locations = (np.where(new_grid == 'A'))
a_count = len(locations[0])

# Process them
total_found = 0

count = 0
while count < a_count:
    x = locations[0][count]
    y = locations[1][count]
    if boundary_check(lines,line_length,[x,y]) == True:
        count += 1
        continue
    else:
        neighbours = get_diag_neighbours(x,y)
        if check_neighbours(neighbours):
            total_found += 1
        count += 1

print(total_found)