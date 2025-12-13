# Write your solution here
def transpose(matrix: list):
    transposed = []
    rows = len(matrix)
    i = 0
    while i < rows:
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        transposed.append(new_row)
        i += 1
    matrix.clear()
    matrix.extend(transposed)
