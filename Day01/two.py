#! /usr/bin/env python3

f = open("input.txt", "r")

first = []
second = []

for line in f.read().splitlines():
    values = line.split()
    first.append(values[0])
    second.append(values[1])

first.sort()
second.sort()

results = 0

for value in first:
    appearances = second.count(value)
    if appearances >= 1:
        results += int(value) * appearances

print(results)
