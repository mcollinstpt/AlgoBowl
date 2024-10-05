import random

def isValid(array):
    print("to do")

def countViolations(array):
    print("to do")

bigArray = []

with open("input_backup.txt") as input:
    firstLine = input.readline().split()
    rows = firstLine[0]
    cols = firstLine[1]

    for line in input:
        bigArray.append(list(line))

unlitCells = False
for i in range(0, len(bigArray)):
    for j in range(0, len(bigArray[i])):
        if(bigArray[i][j] == "."):
            unlitCells = True
            break
    if(unlitCells):
        break

prevViolations = 1000000000
numReplications = 10
bestArray = []
if unlitCells:
    for i in range(0, numReplications):
        invalid = False
        tempArray = bigArray
        while invalid:
            randomRow = random.randrange(0, len(bigArray))
            randomCol = random.randrange(0, len(bigArray[randomRow]))
            if tempArray[randomRow][randomCol] == '.':
                changeToBulb(randomRow, randomCol, tempArray)
            invalid = isValid(tempArray)
        violations = countViolations(tempArray)
        if violations < prevViolations:
            bestArray = tempArray
