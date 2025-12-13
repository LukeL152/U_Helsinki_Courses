# Write your solution here
def anagrams(string1, string2):
    sorted1 = sorted(string1)
    sorted2 = sorted(string2)

    return sorted1 == sorted2
