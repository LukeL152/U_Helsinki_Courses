# Write your solution here


def spruce(x):
    print("a spruce!")
    i = 1
    stars = 1

    # Tree Section
    while i <= x:
        spaces = x - i
        print(" " * spaces + "*" * stars)
        stars += 2
        i += 1

    # Trunk
    print(" " * (x - 1) + "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)

