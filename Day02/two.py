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
        direction = "same"
        report.pop(1)
        return report

    start = report[0]
    i=1
    while i < len(report):
        if direction == "up":
            if report[i] == start + 1 or report[i] == start + 2 or report[i] == start + 3:
                start = report[i]
                i += 1
            else:
                report.pop(i)
                return report

        elif direction == "down":
            if report[i] == start - 1 or report[i] == start - 2 or report[i] == start - 3:
                start = report[i]
                i += 1
            else:
                report.pop(i)
                return report
    
    return report



f = open("input.txt", "r")

reprocess_queue = []
passed = 0

# First pass

for line in f.read().splitlines():
    report = [int(x) for x in line.split()]
    original_report = report.copy()
    processed_report = check_report(report)
    
    if original_report == processed_report:
        passed += 1
    else:
        reprocess_queue.append(processed_report)

redo = len(reprocess_queue)
print(f"Finished first pass - success = {passed}, reprocess = {redo}")

# Reruns

for rerun in reprocess_queue:
    original_rerun = rerun.copy()
    processed_rerun = check_report(rerun)

    if original_rerun == processed_rerun:
        passed += 1
        #print(original_rerun, processed_rerun)
    else:
        print(original_rerun, processed_rerun)
        True

print(passed)
