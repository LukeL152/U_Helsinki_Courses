# Write your solution here
def distinct_numbers(integers):
    distinct_nums = []
    integers.sort()

    for i in integers:
        if i not in distinct_nums:
            distinct_nums.append(i)
    return distinct_nums
