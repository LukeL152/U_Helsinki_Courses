# Copy here code of line function from previous exercise
def line(x, string):
    if string == "":
        print(f"{'*' * x}")
    else:
        print(f"{string[0:1] * x}")


def triangle(size):
    # You should call function line here with proper parameters
    iteration = 1
    while iteration < size + 1:
        layer_size = iteration
        line(layer_size, "#")

        iteration += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
