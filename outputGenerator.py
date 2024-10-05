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
def numberFunc(i, j, bigArray, counter, unlitCells):
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
                changeToBulb(i,j,bigArray,unlitCells)
        if(i != len(bigArray)-1):
            if(bigArray[i+1][j] == "."):
                changeToBulb(i,j,bigArray,unlitCells)
        if(j != 0):
            if(bigArray[i][j-1] == "."):
                changeToBulb(i,j,bigArray,unlitCells)
        if(j != len(bigArray[i])-1):
            if(bigArray[i][j+1] == "."):
                changeToBulb(i,j,bigArray,unlitCells)

def changeToBulb(i, j, bigArray, unlitCells):
    bigArray[i][j] = "L"
    if((i,j) in unlitCells):
        unlitCells.remove((i,j))
    for cell in range(i+1, len(bigArray)-1):
        if(bigArray[cell][j] == "."):
            bigArray[cell][j] = "*"
            if((cell,j) in unlitCells):
                unlitCells.remove((cell,j))
        elif(bigArray[cell][j] != "*"):
            break
    for cell in range(j+1, len(bigArray[i])-1):
        if(bigArray[i][cell] == "."):
            bigArray[i][cell] = "*"
            if((i,cell) in unlitCells):
                unlitCells.remove((i,cell))
        elif(bigArray[i][cell] != "*"):
            break
    for cell in range(i-1, 0, -1):
        if(bigArray[cell][j] == "."):
            bigArray[cell][j] = "*"
            if((cell,j) in unlitCells):
                unlitCells.remove((cell,j))
        elif(bigArray[cell][j] != "*"):
            break
    for cell in range(j-1, 0, -1):
        if(bigArray[i][cell] == "."):
            bigArray[i][cell] = "*"
            if((j,cell) in unlitCells):
                unlitCells.remove((j,cell))
        elif(bigArray[i][cell] != "*"):
            break

def findLitLight(i,j,bigArray):
    for cell in range(i+1, len(bigArray)-1):
        if(bigArray[cell][j] == "L"):
            bigArray[i][j] = "B"
            break
    for cell in range(j+1, len(bigArray[i])-1):
        if(bigArray[i][cell] == "L"):
            bigArray[i][j] = "B"
            break
    for cell in range(i-1, 0, -1):
        if(bigArray[cell][j] == "L"):
            bigArray[i][j] = "B"
            break
    for cell in range(j-1, 0, -1):
        if(bigArray[i][cell] == "L"):
            bigArray[i][j] = "B"
            break

# surroundedFunction/unlitFunction
# reads in .'s to find single cell lights
def surrounded(i, j, bigArray, counter,unlitCells):
    # checking corners
    if (i == 0):
        # upper left
        if (j == 0):
            if ((bigArray[i+1][j] in "X123") and (bigArray[i][j+1] in "X123")):
                changeToBulb(i, j, bigArray,unlitCells)
                counter += 1
        # upper right
        if (j == len(bigArray[i])):
            if ((bigArray[i+1][j] in "X123") and (bigArray[i][j-1] in "X123")):
                changeToBulb(i, j, bigArray,unlitCells)
                counter += 1

    if (i == len(bigArray)):
        # lower left
        if (j == 0):
            if ((bigArray[i-1][j] in "X123") and (bigArray[i][j+1] in "X123")):
                changeToBulb(i, j, bigArray)
                counter += 1       
                #lower right
        if (j == len(bigArray[i])):
            if ((bigArray[i-1][j] in "X123") and (bigArray[i][j-1] in "X123")):
                changeToBulb(i, j, bigArray)
                counter += 1

    # non corners
    if(i!=0 and j!=0 and i!=len(bigArray)-1 and j!=len(bigArray[i])-1):
        if ( (bigArray[i-1][j] in "X123") and (bigArray[i+1][j] in "X123") and (bigArray[i][j+1] in "X123") and (bigArray[i][j-1] in "X123")):
            changeToBulb(i, j, bigArray,unlitCells)
            counter += 1

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

def countViolations(bigArray):
    numVi = 0
    for i in range(0, len(bigArray)):
        for j in range(0, len(bigArray[i])):
            if(bigArray[i][j] == "B"):
                numVi += 1
            elif(bigArray[i][j] != "*" and bigArray[i][j] != "L" and bigArray[i][j] != "X"):
                verifyNumbers(i,j,bigArray,numVi)
    return numVi

def verifyNumbers(i,j,bigArray,viCount):
    bulbs = 0
    if(i != 0):
        if(bigArray[i-1][j] in "LB"):
            bulbs += 1
    if(i != len(bigArray)-1):
        if(bigArray[i+1][j] in "LB"):
            bulbs += 1
    if(j != 0):
        if(bigArray[i][j-1] in "LB"):
            bulbs += 1
    if(j != len(bigArray[i])-1):
        if(bigArray[i][j+1] in "LB"):
            bulbs += 1
    if(bulbs != int(bigArray[i][j])):
        viCount+=1
#     if(i!=0, i!= maxI...)
#         if(i+1 == "X" and i-1== "X", ...):
#             replace with *

# open the input File

bigArray = []
unlitCells = []
lights = []

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
# known lights method
# while true:
#     counter = 0
#     for i in range 0, len(bigarray)
#         for j in range 0, len(bigarray[i])
#             bunch of ifs
#             ex: if(symbol != ".", "X"):
#                     do numberfunction
#     if counter == 0
#         break
while True:
    counter = 0
    for i in range(0, len(bigArray)):
        for j in range(0,len(bigArray[i])):
            if(not (bigArray[i][j] in ".*LX")):
                numberFunc(i,j,bigArray,counter,unlitCells)
            if(bigArray[i][j] == "."):
                surrounded(i,j,bigArray,counter,unlitCells)
    if(counter == 0):
        break
# check if any unlit cells remain
# minViolations = 10000000000000
# if they do:
#     for i in 0,numReplications
#         random :)
#         randomly change unlit squares to lightbulbs
#         fill the rest of unlit cells with bulbs
#         count violations
#         if violations < minViolations
#             save grid

prevViolations = 1000000000
numReplications = 1
bestArray = []
if len(unlitCells) > 0:
    for i in range(0, numReplications):
        lights = []
        invalid = True
        tempArray = bigArray
        while invalid:
            randomCell = random.randrange(0, len(unlitCells))
            if tempArray[unlitCells[randomCell][0]][unlitCells[randomCell][1]] == '.':
                changeToBulb(unlitCells[randomCell][0], unlitCells[randomCell][1], tempArray, unlitCells)
            invalid = isValid(tempArray)
            if(len(unlitCells) == 0):
                break
            print(bigArray)
            print(unlitCells)
        print("end while")
        for light in lights:
            findLitLight(light[0],light[1],tempArray)
        print(bigArray)
        violations = countViolations(tempArray)
        if(violations < prevViolations):
            bestArray = tempArray


# turn grid back to normal ("*" == "." and so forth)