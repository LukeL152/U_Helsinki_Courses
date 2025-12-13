# Write your solution here
def shortest(strings):
    num_items = len(strings)
    length = len(strings[0])
    string = strings[0]
    i = 0
    while i < num_items:
        if len(strings[i]) < length:
            length = len(strings[i])
            string = strings[i]
        i += 1
    return string
