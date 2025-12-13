# Write your solution here
def everything_reversed(strings: list):
    rev_strings = []
    rev_list = strings.copy()
    rev_list.reverse()
    length = len(strings)
    i = 0
    while i < length:
        string = rev_list[i]
        rev = string[::-1]
        rev_strings.append(rev)
        i += 1
    return rev_strings
