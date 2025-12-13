# Write your solution here
def histogram(string):
    char_count = {}
    for char in string:
        count = string.count(char)
        char_count[char] = count
    for key in char_count:
        print(f"{key} {'*' * char_count[key]}")
