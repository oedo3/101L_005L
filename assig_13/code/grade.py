import math
def total(value):
    sum = 0
    for i in value:
        sum += i
    return sum
def average(value):
    if len(value) == 0:
        return math.nan
    average = total(value) / len(value)
    return average
def median(value):
    if len(value) == 0:
        raise ValueError
    if len(value) % 2 == 1:
        median = sorted(value)[len(value)//2]
        return median
    else:
        x = sorted(value)[len(value)//2]
        y = sorted(value)[(len(value)//2) - 1]
        median = average([x, y])
        return median