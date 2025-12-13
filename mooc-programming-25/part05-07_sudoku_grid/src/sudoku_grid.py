# Write your solution here:
def row_correct(sudoku: list, row_no: int):
    for i in range(1, 10):
        if sudoku[row_no].count(i) <= 1:
            continue
        elif sudoku[row_no].count(i) > 1:
            return False
    return True


def column_correct(sudoku: list, column_no: int):
    col = []
    for row in sudoku:
        col.append(row[column_no])
    for j in range(1, 10):
        if col.count(j) <= 1:
            continue
        elif col.count(j) > 1:
            return False
    return True


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


def sudoku_grid_correct(sudoku: list):
    rows = len(sudoku)
    for i in range(0, rows):
        if row_correct(sudoku, i):
            continue
        elif not row_correct(sudoku, i):
            return False

    columns = len(sudoku[0])
    for i in range(0, columns):
        if column_correct(sudoku, i):
            continue
        elif not column_correct(sudoku, i):
            return False

    blocks = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    for block in blocks:
        row = block[0]
        col = block[1]
        if block_correct(sudoku, row, col):
            continue
        elif not block_correct(sudoku, row, col):
            return False
    return True
