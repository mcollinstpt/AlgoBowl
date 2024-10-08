import random
import sys

# numberFunction:
#     if(num == 3 and i == 0 and j!=0 and j!= maxJ)
#         j-1 == *
#         j+1==*
#         i+1==*
#     if(num==3 and i==maxI and...)
#         ...
#     if(num == 3 and i!=0...)
#         check how many spots around are available
#         if unlit == 3
#             place *
#             counter += 1
def numberFunc(i, j, bigArray, counter, unlitCells, lightList):
    unlit = 0
    if(i != 0):
        if(bigArray[i-1][j] == "."):
            unlit += 1
    if(i != len(bigArray)-1):
        if(bigArray[i+1][j] == "."):
            unlit += 1
    if(j != 0):
        if(bigArray[i][j-1] == "."):
            unlit += 1
    if(j != len(bigArray[i])-1):
        if(bigArray[i][j+1] == "."):
            unlit += 1
    if(unlit == int(bigArray[i][j]) or (unlit == 4 and int(bigArray[i][j]) > 4)):
        counter += 1
        if(i != 0):
            if(bigArray[i-1][j] == "."):
                changeToBulb(i-1,j,bigArray,unlitCells,lightList)
        if(i != len(bigArray)-1):
            if(bigArray[i+1][j] == "."):
                changeToBulb(i+1,j,bigArray,unlitCells, lightList)
        if(j != 0):
            if(bigArray[i][j-1] == "."):
                changeToBulb(i,j-1,bigArray,unlitCells, lightList)
        if(j != len(bigArray[i])-1):
            if(bigArray[i][j+1] == "."):
                changeToBulb(i,j+1,bigArray,unlitCells, lightList)

def changeToBulb(i, j, bigArray, unlitCells, lightList):
    bigArray[i][j] = "L"
    lightList.append((i,j))
    if((i,j) in unlitCells):
        unlitCells.remove((i,j))
    # down
    for cell in range(i+1, len(bigArray)):
        if(bigArray[cell][j] == "."):
            bigArray[cell][j] = "*"
            if((cell,j) in unlitCells):
                unlitCells.remove((cell,j))
        elif(bigArray[cell][j] in "0123X"):
            break
    # left
    for cell in range(j+1, len(bigArray[i])):
        if(bigArray[i][cell] == "."):
            bigArray[i][cell] = "*"
            if((i,cell) in unlitCells):
                unlitCells.remove((i,cell))
        elif(bigArray[i][cell] in "0123X"):
            break
    for cell in range(i-1, -1, -1):
        if(bigArray[cell][j] == "."):
            bigArray[cell][j] = "*"
            if((cell,j) in unlitCells):
                unlitCells.remove((cell,j))
        elif(bigArray[cell][j] in "0123X"):
            break
    for cell in range(j-1, -1, -1):
        if(bigArray[i][cell] == "."):
            bigArray[i][cell] = "*"
            if((j,cell) in unlitCells):
                unlitCells.remove((j,cell))
        elif(bigArray[i][cell] in "0123X"):
            break

def findLitLight(i,j,wackyArray):
    for cell in range(i+1, len(wackyArray)):
        if(wackyArray[cell][j] == "L" or wackyArray[cell][j] == "B"):
            wackyArray[i][j] = "B"
            break
        elif(wackyArray[cell][j] in "01234X"):
            break
    for cell in range(j+1, len(wackyArray[i])):
        if(wackyArray[i][cell] == "L" or wackyArray[i][cell] == "B"):
            wackyArray[i][j] = "B"
            break
        elif(wackyArray[i][cell] in "01234X"):
            break
    for cell in range(i-1, -1, -1):
        if(wackyArray[cell][j] == "L" or wackyArray[cell][j] == "B"):
            wackyArray[i][j] = "B"
            break
        elif(wackyArray[cell][j] in "01234X"):
            break
    for cell in range(j-1, -1, -1):
        if(wackyArray[i][cell] == "L" or wackyArray[i][cell] == "B"):
            wackyArray[i][j] = "B"
            break
        elif(wackyArray[i][cell] in "01234X"):
            break

# surroundedFunction/unlitFunction
# reads in .'s to find single cell lights
def surrounded(i, j, bigArray, counter,unlitCells, lightList):
    # checking corners
    if (i == 0):
        # upper left
        if (j == 0):
            if ((bigArray[i+1][j] in "X123") and (bigArray[i][j+1] in "X123")):
                changeToBulb(i, j, bigArray,unlitCells, lightList)
                counter += 1
        # upper right
        if (j == len(bigArray[i])):
            if ((bigArray[i+1][j] in "X123") and (bigArray[i][j-1] in "X123")):
                changeToBulb(i, j, bigArray,unlitCells, lightList)
                counter += 1

    if (i == len(bigArray)):
        # lower left
        if (j == 0):
            if ((bigArray[i-1][j] in "X123") and (bigArray[i][j+1] in "X123")):
                changeToBulb(i, j, bigArray, lightList)
                counter += 1       
                #lower right
        if (j == len(bigArray[i])):
            if ((bigArray[i-1][j] in "X123") and (bigArray[i][j-1] in "X123")):
                changeToBulb(i, j, bigArray, lightList)
                counter += 1

    # non corners
    if(i!=0 and j!=0 and i!=len(bigArray)-1 and j!=len(bigArray[i])-1):
        if ( (bigArray[i-1][j] in "X123") and (bigArray[i+1][j] in "X123") and (bigArray[i][j+1] in "X123") and (bigArray[i][j-1] in "X123")):
            changeToBulb(i, j, bigArray,unlitCells, lightList)
            counter += 1

def isValid(array):
    unlitCells2 = False
    print("Not valid")
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

bigArray = []
unlitCells = []
lights = []

# opening file
with open(sys.argv[1]) as input:
    firstLine = input.readline().replace("\n","").split()
    rows = firstLine[0]
    cols = firstLine[1]

    for line in input:
        bigArray.append(list(line.replace("\n","")))

# turn into an array of arrays
# each line in the input file = one index of big array
for i in range(0, len(bigArray)):
    for j in range(0,len(bigArray[i])):
        if(bigArray[i][j] == "."):
            unlitCells.append((i,j))

while True:
    counter = 0
    for i in range(0, len(bigArray)):
        for j in range(0,len(bigArray[i])):
            if(not (bigArray[i][j] in ".*LX")):
                numberFunc(i,j,bigArray,counter,unlitCells, lights)
            if(bigArray[i][j] == "."):
                surrounded(i,j,bigArray,counter,unlitCells, lights)
    if(counter == 0):
        break

minViolations = 1000000000
numReplications = 1000
bestArray = []
if len(unlitCells) > 0:
    for i in range(0, numReplications):
        tempLights = lights[:]
        invalid = True
        tempArray = bigArray[:]
        while invalid:
            if(len(unlitCells) == 0):
                break
            randomCell = random.randrange(0, len(unlitCells))
            if tempArray[unlitCells[randomCell][0]][unlitCells[randomCell][1]] == '.':
                changeToBulb(unlitCells[randomCell][0], unlitCells[randomCell][1], tempArray, unlitCells, tempLights)
            invalid = isValid(tempArray)
        for light in tempLights:
            findLitLight(light[0],light[1],tempArray)
        violations = countViolations(tempArray)
        if(violations < minViolations):
            bestArray = tempArray[:]
            minViolations = violations

outputFile = open(sys.argv[2], "w")
outputFile.write(str(minViolations))
outputFile.write("\n")
for i in range(0,len(bestArray)):
    for j in range(0,len(bestArray[i])):
        if(bestArray[i][j] == "*"):
            outputFile.write(".")
        elif(bestArray[i][j] == "B"):
            outputFile.write("L")
        else:
            outputFile.write(bigArray[i][j])
    if (i != len(bestArray) - 1):
        outputFile.write("\n")

outputFile.close()