#! /usr/bin/env python3

def check_report(report):
    # Establish direction
    a = report[0]
    b = report[1]
    if b > a:
        direction = "up"
    elif a > b:
        direction = "down"
    elif a == b:
        return [report, "fail"]

    start = report[0]
    i=1
    while i < len(report):
        if direction == "up":
            if report[i] == start + 1 or report[i] == start + 2 or report[i] == start + 3:
                start = report[i]
                i += 1
            else:
                return [report, "fail"]

        elif direction == "down":
            if report[i] == start - 1 or report[i] == start - 2 or report[i] == start - 3:
                start = report[i]
                i += 1
            else:
                return [report, "fail"]
    
    return [report, "pass"]


f = open("input.txt", "r")

reprocess_queue = []
passed = 0

# First pass

for line in f.read().splitlines():
    report = [int(x) for x in line.split()]
    result = check_report(report)

    if result[1] == "pass":
        passed += 1
    else:
        reprocess_queue.append(result[0])

# Reprocess those that failed, brutally

for rerun in reprocess_queue:
    length = len(rerun)
    i = 0
    while i < length:
        rerun_bkp = rerun.copy()
        rerun.pop(i)
        result = check_report(rerun)
        if result[1] == "pass":
            passed += 1
            break
        else:
            rerun = rerun_bkp.copy()
            i += 1

print(passed)