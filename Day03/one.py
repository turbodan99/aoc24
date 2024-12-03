#! /usr/bin/env python3

import re

f = open("input.txt", "r")

result = 0

for line in f.read().splitlines():
    matches = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
    for match in matches:
        values = (match.strip("mul()"))
        seperate = values.split(',')
        result += int(seperate[0]) * int(seperate[1])

print(result)