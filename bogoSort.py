import random
import sys

def isValid(array):
    unlitCells2 = False
    for i in range(0, len(bigArray)):
        for j in range(0, len(bigArray[i])):
            if(bigArray[i][j] == "."):
                unlitCells2 = True
                break
        if(unlitCells2):
            break
    return unlitCells2

def countViolations(coolArray):
    numVi = 0
    for i in range(0, len(coolArray)):
        for j in range(0, len(coolArray[i])):
            if(coolArray[i][j] == "B"):
                numVi += 1
            elif(coolArray[i][j] != "*" and coolArray[i][j] != "L" and coolArray[i][j] != "B" and coolArray[i][j] != "X"):
                numVi += verifyNumbers(i,j,coolArray)
    return numVi

def verifyNumbers(i,j,bigArray):
    viCount = 0
    bulbs = 0
    if(i != 0):
        if(bigArray[i-1][j] == "L" or bigArray[i-1][j] == "B"):
            bulbs += 1
    if(i != len(bigArray)-1):
        if(bigArray[i+1][j] == "L" or bigArray[i+1][j] == "B"):
            bulbs += 1
    if(j != 0):
        if(bigArray[i][j-1] == "L" or bigArray[i][j-1] == "B"):
            bulbs += 1
    if(j != len(bigArray[i])-1):
        if(bigArray[i][j+1] == "L" or bigArray[i][j+1] == "B"):
            bulbs += 1
    if(bulbs != int(bigArray[i][j])):
        viCount+=1
    return viCount

def changeToBulb(i, j, bigArray, lightList):
    bigArray[i][j] = "L"
    lightList.append((i,j))
    for cell in range(i+1, len(bigArray)-1):
        if(bigArray[cell][j] == "."):
            bigArray[cell][j] = "*"
        elif(bigArray[cell][j] != "*"):
            break
    for cell in range(j+1, len(bigArray[i])-1):
        if(bigArray[i][cell] == "."):
            bigArray[i][cell] = "*"
        elif(bigArray[i][cell] != "*"):
            break
    for cell in range(i-1, 0, -1):
        if(bigArray[cell][j] == "."):
            bigArray[cell][j] = "*"
        elif(bigArray[cell][j] != "*"):
            break
    for cell in range(j-1, 0, -1):
        if(bigArray[i][cell] == "."):
            bigArray[i][cell] = "*"
        elif(bigArray[i][cell] != "*"):
            break

def findLitLight(i,j,wackyArray):
    for cell in range(i+1, len(wackyArray)):
        if(wackyArray[cell][j] == "L" or wackyArray[cell][j] == "B"):
            wackyArray[i][j] = "B"
            break
    for cell in range(j+1, len(wackyArray[i])):
        if(wackyArray[i][cell] == "L" or wackyArray[i][cell] == "B"):
            wackyArray[i][j] = "B"
            break
    for cell in range(i-1, -1, -1):
        if(wackyArray[cell][j] == "L" or wackyArray[cell][j] == "B"):
            wackyArray[i][j] = "B"
            break
    for cell in range(j-1, -1, -1):
        if(wackyArray[i][cell] == "L" or wackyArray[i][cell] == "B"):
            wackyArray[i][j] = "B"
            break

bigArray = []

with open(sys.argv[1]) as input:
    firstLine = input.readline().split()
    rows = firstLine[0]
    cols = firstLine[1]

    for line in input:
        bigArray.append(list(line.replace("\n","")))

unlitCells = False
for i in range(0, len(bigArray)):
    for j in range(0, len(bigArray[i])):
        if(bigArray[i][j] == "."):
            unlitCells = True
            break
    if(unlitCells):
        break

prevViolations = 1000000000
numReplications = 1000000000
bestArray = []
if unlitCells:
    for i in range(0, numReplications):
        invalid = True
        tempArray = bigArray.copy()
        tempLights = []
        while invalid:
            randomRow = random.randrange(0, len(bigArray))
            randomCol = random.randrange(0, len(bigArray[randomRow]))
            if tempArray[randomRow][randomCol] == '.':
                changeToBulb(randomRow, randomCol, tempArray, tempLights)
            invalid = isValid(tempArray)
        for light in tempLights:
            findLitLight(light[0],light[1],tempArray)
        violations = countViolations(tempArray)
        if violations < prevViolations:
            bestArray = tempArray.copy()

outputFile = open(sys.argv[2], "w")
outputFile.write(str(violations))
outputFile.write("\n")
for i in range(0,len(bestArray)):
    for j in range(0,len(bestArray[i])):
        if(bestArray[i][j] == "*"):
            outputFile.write(".")
        elif(bestArray[i][j] == "B"):
            outputFile.write("L")
        else:
            outputFile.write(bigArray[i][j])
    outputFile.write("\n")

outputFile.close()