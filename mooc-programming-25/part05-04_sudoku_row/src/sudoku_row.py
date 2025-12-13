# Write your solution here
def row_correct(sudoku: list, row_no: int):
    for i in range(1, 10):
        if sudoku[row_no].count(i) <= 1:
            continue
        elif sudoku[row_no].count(i) > 1:
            return False
    return True
