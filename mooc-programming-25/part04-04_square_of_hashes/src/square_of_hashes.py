# Copy here code of line function from previous exercise
def line(x, string):
    if string == "":
        print(f"{'*' * x}")
    else:
        print(f"{string[0:1] * x}")


def square_of_hashes(size):
    # You should call function line here with proper parameters
    iteration = 0
    while iteration < size:
        line(size, "#")
        iteration += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
