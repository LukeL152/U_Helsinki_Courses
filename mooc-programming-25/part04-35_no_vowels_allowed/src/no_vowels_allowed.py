# Write your solution here
def no_vowels(string):
    vowels = "aeiou"
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result
