def solve(sudoku):
    place = find_empty(sudoku)

    if not place:
        return True

    row,col = place

    for x in range(1,10):
        if valid(sudoku, x, place):
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

def valid(sudoku, value, pos):
    #check row
    for i in range(len(sudoku[0])):
        if sudoku[pos[0]][i] == value and pos[1] != i:
            return False

    #check column
    for i in range(len(sudoku)):
        if sudoku[i][pos[1]] == value and pos[0] != i:
            return False

    #check block
    rowStart = pos[0] // 3 * 3
    columnStart = pos[1] // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[rowStart+i][columnStart+j] == value and pos != (rowStart+i,columnStart+j):
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
