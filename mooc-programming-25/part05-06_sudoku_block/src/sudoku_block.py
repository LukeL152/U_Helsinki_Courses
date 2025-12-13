# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    check = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            check.append(sudoku[i][j])
    for x in range(1, 10):
        if check.count(x) <= 1:
            continue
        elif check.count(x) > 1:
            return False
    return True
