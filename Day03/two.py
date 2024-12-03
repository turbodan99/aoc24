#! /usr/bin/env python3

import re

def process_batch(batch):
    result = 0
    matches = re.findall(r"mul\([0-9]+,[0-9]+\)", batch)
    for match in matches:
        values = (match.strip("mul()"))
        seperate = values.split(',')
        result += int(seperate[0]) * int(seperate[1])
    return result


f = open("input.txt", "r")

bigline = ""
grand_total = 0

# Read input into one big string

for char in f.read():
    bigline = bigline + char

#split it on donts

listed = bigline.split('don\'t()')

#process first element (implicit do)

grand_total += process_batch(listed[0])

# for each subsequent element, strip to the first do and process the rest

for batch in listed[1:]:
    pos = batch.find('do()')
    if pos > 1:
        trimmed = batch[pos:]
        grand_total += process_batch(trimmed)
    
# final total
print(grand_total)