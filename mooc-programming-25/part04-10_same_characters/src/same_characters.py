# Write your solution here


def same_chars(string, x, y):
    return string[x : x + 1] == string[y : y + 1]


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("simsalabim", 1, 8))
