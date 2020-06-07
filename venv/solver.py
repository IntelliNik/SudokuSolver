def solve(sudoku):
    place = find_empty(sudoku)

    if not place:
        return True

    row, col = place
    for x in range(1,10):
        if valid(sudoku, row, col, x):
            sudoku[row][col] = x

            if solve(sudoku):
                return True

            sudoku[row][col] = 0

    return False

def find_empty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i,j)
    return None

def valid(soduoku, row, col, value):
    #check row
    for i in range(len(sudoku[0])):
        if sudoku[row][i] == value:
            return False

    #check column
    for i in range(len(sudoku)):
        if sudoku[i][col] == value:
            return False

    #check block
    rowStart = row // 3 * 3
    columnStart = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[rowStart+i][columnStart+j] == value:
                return False
    return True

def printSudoku(sudoku):
    print("--------SUDOKU--------")
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("")

        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")


sudoku = [
    [6,5,0,0,0,8,0,0,0],
    [7,0,1,0,4,0,0,0,0],
    [0,0,0,0,0,0,0,8,0],
    [0,0,0,0,3,1,9,0,6],
    [0,0,4,0,7,0,3,0,0],
    [1,0,7,6,2,0,0,0,0],
    [0,4,0,0,0,0,0,0,0],
    [0,0,0,0,8,0,6,0,2],
    [0,0,0,9,0,0,0,5,8],
]

solve(sudoku)
printSudoku(sudoku)
