# Write your solution here
def most_common_character(string):
    count_prev = 0
    for i in string:
        count = string.count(i)
        if count > count_prev:
            count_prev = count
            most_common = i
    return most_common
