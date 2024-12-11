"""
// Part 1
many reports
one report per line
each report is list of numbers called levels separated by spaces
a report is safe if levels are either increasing or decreasing
any two adjacent levels differ by at least one and at most three

// Part 2
attempt to remove one level and check
"""

input_file = 'input.txt'

def count_safe_reports(input_file: str):
    """Count number of safe reports"""
    safe_count = 0
    with open(input_file, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_report or is_safe_with_dampener(report): # could be more efficient because lesser computation on is_safe_with_dampener
                safe_count += 1
    return safe_count

def is_safe_report(report: list[int]):
    """Check safe report condition"""
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are within the bounds [1, 3] or [-3, -1]
    if all(1 <= diff <= 3 for diff in differences):  # Increasing
        return True
    if all(-3 <= diff <= -1 for diff in differences):  # Decreasing
        return True
    
    return False

def is_safe_with_dampener(report: list[int]):
    """Check if report can be safe by removing one level"""
    for i in range(len(report)):
        # Merge a new report by excluding current index
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    return False

safe_reports = count_safe_reports(input_file)
print(f"Safe reports: {safe_reports}")




