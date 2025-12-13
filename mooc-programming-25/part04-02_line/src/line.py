# Write your solution here
def line(x, string):
    if string == "":
        print(f"{'*' * x}")
    else:
        print(f"{string[0:1] * x}")
    # test


if __name__ == "__main__":
    line(5, "x")
