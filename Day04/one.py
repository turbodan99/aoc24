#! /usr/bin/env python3

import numpy as np
import re

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

total_matches = 0

# Extract each row, read in both directions, count the XMASs
count = 0
while count < lines:
    string = ""
    for x in new_grid[count]:
        string = string + x
    
    matches = re.findall(r"XMAS", string)
    total_matches += len(matches)
    rev_matches = re.findall(r"XMAS", string[::-1])
    total_matches += len(rev_matches)
    count += 1

# Extract each column, read in both directions, count the XMASs
count = 0
while count < line_length:
    string = ""
    for x in new_grid[:,count]:
        string = string + x
    
    matches = re.findall(r"XMAS", string)
    total_matches += len(matches)
    rev_matches = re.findall(r"XMAS", string[::-1])
    total_matches += len(rev_matches)
    count += 1

# Extract each diagonal read in both directions, count the XMASs
diag = -abs(line_length)

while diag <= abs(line_length):
    content = np.diagonal(new_grid, offset=diag)
    string = ""
    for x in content:
        string = string + x
    matches = re.findall(r"XMAS", string)
    total_matches += len(matches)
    rev_matches = re.findall(r"XMAS", string[::-1])
    total_matches += len(rev_matches)
    diag += 1

# Flip array for second lot
diag = -abs(lines)

while diag <= abs(lines):
    content = np.flipud(new_grid).diagonal(offset=diag)
    string = ""
    for x in content:
        string = string + x
    matches = re.findall(r"XMAS", string)
    total_matches += len(matches)
    rev_matches = re.findall(r"XMAS", string[::-1])
    total_matches += len(rev_matches)
    diag += 1

print(total_matches)