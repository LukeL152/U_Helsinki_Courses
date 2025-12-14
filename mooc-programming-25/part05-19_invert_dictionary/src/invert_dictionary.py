# Write your solution here
def invert(dictionary: dict):
    temp_dict = dictionary.copy()
    dictionary.clear()
    for key, value in temp_dict.items():
        dictionary[value] = key

