# Write your solution here
def all_the_longest(strings):
    num_items = len(strings)
    length = len(strings[0])
    new_list = []
    i = 0
    while i < num_items:
        if len(strings[i]) > length:
            length = len(strings[i])
        i += 1
    i = 0
    while i < num_items:
        if len(strings[i]) == length:
            new_list.append(strings[i])
        i += 1
    return new_list
