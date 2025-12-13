# Copy here code of line function from previous exercise
def line(x, string):
    if string == "":
        print(f"{'*' * x}")
    else:
        print(f"{string[0:1] * x}")


def box_of_hashes(height):
    # You should call function line here with proper parameters
    iteration = 0
    while iteration < height:
        line(10, "#")
        iteration += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
