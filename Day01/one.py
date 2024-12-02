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

for i in range(len(first)):
    vals = [int(first[i]), int(second[i])]
    vals.sort()
    diff = vals[1] - vals[0]
    results += diff

print(results)


