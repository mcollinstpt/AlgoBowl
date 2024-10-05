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
#                     do unlit function
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
prevViolations = 1000000000
numReplications = 10
bestArray = []
if unlitCells:
    for i in range(0, numReplications):
        invalid = false
        tempArray = bigArray
        while invalid:
            randomRow = random.randrange(0, len(bigArray))
            randomCol = random.randrange(0, len(smallArray))
            if tempArray[randomRow][randomCol] == '.':
                changeToBulb(randomeRow, randomCol, tempArray)
            invalid = isValid(tempArray)
        violations = countViolations(tempArray)
        if violations < prevViolations:
            bestArray = tempArray


# turn grid back to normal ("*" == "." and so forth)