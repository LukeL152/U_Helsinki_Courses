# Write your solution here
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
