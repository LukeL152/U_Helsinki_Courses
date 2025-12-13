# Write your solution here
def longest(strings: list):
    current = 0
    for s in strings:
        length = len(s)
        if length > current:
            current = length
            longest_str = s
    return longest_str
