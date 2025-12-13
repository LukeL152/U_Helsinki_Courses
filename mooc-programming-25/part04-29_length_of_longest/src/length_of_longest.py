# Write your solution here
def length_of_longest(strings):
    length = 0
    for s in strings:
        if len(s) > length:
            length = len(s)
    return length
