import sys

def changeToBulb(i, j, bigArray):
    bigArray[i][j] == "L"
    for cell in range(i+1, len(bigArray)-1):
        if(bigArray[cell][j] == "."):
            bigArray[cell][j] == "*"
        elif(bigArray[cell][j] != "*"):
            break
    for cell in range(j+1, len(bigArray[i])-1):
        if(bigArray[i][cell] == "."):
            bigArray[i][cell] == "*"
        elif(bigArray[i][cell] != "*"):
            break
    for cell in range(i-1, 0, -1):
        if(bigArray[cell][j] == "."):
            bigArray[cell][j] == "*"
        elif(bigArray[cell][j] != "*"):
            break
    for cell in range(j-1, 0, -1):
        if(bigArray[i][cell] == "."):
            bigArray[i][cell] == "*"
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

bigArray = []
with open(sys.argv[1]) as input:
    violations = int(input.readline().replace("\n",""))

    for line in input:
        bigArray.append(list(line.replace("\n","")))

viCount = 0

for i in range(0, len(bigArray)):
    for j in range(0, len(bigArray[i])):
        if(bigArray[i][j] == "L"):
            changeToBulb(i,j,bigArray)
            findLitLight(i,j,bigArray)

invalid = False

for i in range(0, len(bigArray)):
    for j in range(0, len(bigArray[i])):
        if(bigArray[i][j] == "."):
            invalid = True
            break
        elif(bigArray[i][j] == "B"):
            viCount += 1
        elif(bigArray[i][j] != "*" and bigArray[i][j] != "L" and bigArray[i][j] != "X"):
            verifyNumbers(i,j,bigArray,viCount)
    if(invalid):
        break

if(invalid):
    print("INVALID      WRONG       BAD")
    print("Unlit cell located!!!!!!!!")

elif(viCount != violations):
    print("INVALID      WRONG       BAD")
    print("Num Violations:",viCount)
    print("Num predicted violations:",violations)

else:
    print("VALID    CORRECT     GOOD")
