def solve():
    for triple in range(len(sudoku)):
        for element in range(len(sudoku[triple])):
            if(sudoku[triple][element] == 0):
                checkPossibleCanidates(triple,element)

def checkPossibleCanidates(triple,element):
    canidates = [1,2,3,4,5,6,7,8,9]

    # delete impossible canidates according to block
    offsetColumn = triple % 3
    currentBlock = (triple // 9) * 9 + offsetColumn # round down and set column

    for tripleBlock in range(3):
        for elementBlock in range(3):
            if(sudoku[currentBlock][elementBlock] in canidates):
                canidates.remove(sudoku[currentBlock][elementBlock])
        currentBlock += 3

    #delete impossible canidates according to row
    firstRowElement = (triple - triple % 3)

    for tripleRow in range(firstRowElement, firstRowElement+3):
        for elementRow in range(3):
            if(sudoku[tripleRow][elementRow] in canidates):
                canidates.remove(sudoku[tripleRow][elementRow])

    #delete impossible canidates according to column
    for column in range(9):
        if(sudoku[(column*3)+(triple%3)][element] in canidates):
            canidates.remove(sudoku[(column*3)+(triple%3)][element])

    if (len(canidates) == 1):
        sudoku[triple][element] = canidates[0]
        print(str(triple)+","+str(element)+" wurde ersetzt")

def printSudoku():
    print("------------SUDOKU-------------")
    for x in range(len(sudoku)//3):
        print(str(sudoku[x*3]) + "  " + str(sudoku[x*3+1]) + "  " + str(sudoku[x*3+2]))
        if((x+1) % 3==0):
            print()

sudoku = [
    [6,5,0],[0,0,8],[0,0,0],
    [7,0,1],[0,4,0],[0,0,0],
    [0,0,0],[0,0,0],[0,8,0],
    [0,0,0],[0,3,1],[9,0,6],
    [0,0,4],[0,7,0],[3,0,0],
    [1,0,7],[6,2,0],[0,0,0],
    [0,4,0],[0,0,0],[0,0,0],
    [0,0,0],[0,8,0],[6,0,2],
    [0,0,0],[9,0,0],[0,5,8],
]

for x in range(17):
    print("----next----")
    solve()
printSudoku()
