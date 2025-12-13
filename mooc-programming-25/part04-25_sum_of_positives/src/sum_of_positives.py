# Write your solution here
def sum_of_positives(integers):
    sum = 0
    for i in integers:
        if i > 0:
            sum += i
    return sum

