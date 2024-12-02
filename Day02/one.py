#! /usr/bin/env python3

def check_report(report, direction):
    value = report[0]
    if direction == "increase":
        for x in report[1:]:
            if x == value + 1 or x == value + 2 or x == value + 3:
                print(f"Increase pass - old {value} new {x}")
                value = x
            else:
                print(f"Increase fail - old {value} new {x}")
                return "fail"
        return "pass"
    elif direction == "decrease":
        for x in report[1:]:
            if x == value - 1 or x == value - 2 or x == value - 3:
                print(f"Decrease pass - old {value} new {x}")
                value = x
            else:
                print(f"Decrease fail - old {value} new {x}")
                return "fail"
        return "pass"


f = open("input.txt", "r")
count = 0

for line in f.read().splitlines():
    report = [int(x) for x in line.split()]
    if report[1] > report[0]:
        if check_report(report, "increase") == "pass":
            print("Incremeneting count")
            count += 1
    elif report[1] < report[0]:
        if check_report(report, "decrease") == "pass":
            print("Incremeneting count")
            count += 1

print(count)
