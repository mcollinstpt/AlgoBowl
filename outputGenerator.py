import random

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
def numberFunc(i, j, bigArray, counter, symbol):
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
    if(unlit == int(symbol)):
        counter += 1
        if(i != 0):
            if(bigArray[i-1][j] == "."):
                changeToBulb()
        if(i != len(bigArray)):
            if(bigArray[i+1][j] == "."):
                changeToBulb()
        if(j != 0):
            if(bigArray[i][j-1] == "."):
                changeToBulb()
        if(j != len(bigArray[i])):
            if(bigArray[i][j+1] == "."):
                changeToBulb()

def changeToBulb(i, j, bigArray):
    bigArray[i][j] == "L"
    for cell in range(i+1, len(bigArray)-1):
        if(bigArray[cell][j] == "."):
            bigArray[cell][j] == "*"
        elif(bigArray[cell][j] != "*" and bigArray[i][cell] != "L"):
            break
    for cell in range(j+1, len(bigArray[i])-1):
        if(bigArray[i][cell] == "."):
            bigArray[i][cell] == "*"
        elif(bigArray[i][cell] != "*" and bigArray[i][cell] != "L"):
            break
    for cell in range(i-1, 0, -1):
        if(bigArray[cell][j] == "."):
            bigArray[cell][j] == "*"
        elif(bigArray[cell][j] != "*" and bigArray[i][cell] != "L"):
            break
    for cell in range(j-1, 0, -1):
        if(bigArray[i][cell] == "."):
            bigArray[i][cell] == "*"
        elif(bigArray[i][cell] != "*" and bigArray[i][cell] != "L"):
            break

# unlitFunction:
#     if(i!=0, i!= maxI...)
#         if(i+1 == "X" and i-1== "X", ...):
#             replace with *

# open the input File

# turn into an array of arrays
# each line in the input file = one index of big array

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


# turn grid back to normal ("*" == "." and so forth)