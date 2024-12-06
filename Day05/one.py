#! /usr/bin/env python3

from math import ceil

def check_rules(x,y):
    search = y + "|" + x # is there a rule saying y must come before x
    if search in rules:
        return("fail")
    else:
        return("pass")


def process_update(update):
    check = len(update) -1
    i = 0
    j = 1
    while i < check:
        x = update[i]
        y = update[j]
        result = check_rules(x,y)
        if result == "fail":
            return("fail")
        else:
            i += 1
            j += 1
    return("pass") 


f = open("input.txt", "r")

rules = []
data = []
success = []

for line in f.read().splitlines():
    if line.find("|") == 2:
        rules.append(line)
    elif line.find(",") == 2:
        data.append(line.split(","))

for update in data:
    result = process_update(update)
    if result == "pass":
        success.append(update)    

total = 0

for update in success:
    length = len(update)
    middle_val = int(update[ceil(length / 2) - 1])
    total += middle_val

print(total)