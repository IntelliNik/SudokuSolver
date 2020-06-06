def solve():
    for triple in range(len(sudoku)):
        for element in range(len(sudoku[triple])):
            if(sudoku[triple][element] == 0):
                checkPossibleCanidates(triple,element)
    printSudoku()

def checkPossibleCanidates(triple,element):
    canidates = list(range(1,9))
    firstRowElement = (triple-triple%3)
    print(str(triple) + "," + str(element))

    #delete impossible canidates according to row
    for tripleRow in range(firstRowElement, firstRowElement+3):
        for elementRow in range(3):
            if(sudoku[tripleRow][elementRow] in canidates):
                canidates.remove(sudoku[tripleRow][elementRow])
    print(str(element) + str(canidates))

    #delete impossible canidates according to column
    for column in range(9):
        if(sudoku[(column*3)+(triple%3)][element] in canidates):
            canidates.remove(sudoku[(column*3)+(triple%3)][element])
    print(str(element) + str(canidates))
    if(len(canidates) == 1):
        sudoku[triple][element]=canidates[0]

def printSudoku():
    print("----------SUDOKU-----------")
    for x in range(len(sudoku)//3):
        print(sudoku[x*3] + sudoku[x*3+1] + sudoku[x*3+2])

sudoku = [
    [0,0,4],[0,1,8],[0,0,9],
    [2,0,7],[0,0,0],[1,8,0],
    [0,8,0],[0,3,0],[6,0,0],
    [8,0,0],[0,0,6],[5,9,2],
    [0,0,0],[5,0,1],[3,0,0],
    [0,0,0],[0,8,2],[0,0,0],
    [0,0,6],[0,0,0],[0,0,5],
    [3,2,0],[0,0,7],[4,6,1],
    [0,1,5],[0,6,0],[9,0,7],
]

for x in range(20):
    solve()

