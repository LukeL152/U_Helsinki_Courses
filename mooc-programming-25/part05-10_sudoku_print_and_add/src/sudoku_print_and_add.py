# Write your solution here
def print_sudoku(sudoku):
    for row_index, row in enumerate(sudoku):
        for col_index, value in enumerate(row):
            # Print "_" instead of 0
            cell = "_" if value == 0 else str(value)

            # Print value with NO newline
            print(cell, end=" ")

            # Extra spacing after every 3rd column
            if (col_index + 1) % 3 == 0:
                print(" ", end="")

        print()  # end of row

        # Extra blank line after every 3rd row
        if (row_index + 1) % 3 == 0:
            print()


def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number
