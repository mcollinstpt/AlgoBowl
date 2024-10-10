import sys

def changeToBulb(i, j, bigArray):
    bigArray[i][j] = "L"
    for cell in range(i+1, len(bigArray)):
        if(bigArray[cell][j] == "."):
            bigArray[cell][j] = "*"
        elif(bigArray[cell][j] in "01234X"):
            break
    for cell in range(j+1, len(bigArray[i])):
        if(bigArray[i][cell] == "."):
            bigArray[i][cell] = "*"
        elif(bigArray[i][cell] in "01234X"):
            break
    for cell in range(i-1, -1, -1):
        if(bigArray[cell][j] == "."):
            bigArray[cell][j] = "*"
        elif(bigArray[cell][j] in "01234X"):
            break
    for cell in range(j-1, -1, -1):
        if(bigArray[i][cell] == "."):
            bigArray[i][cell] = "*"
        elif(bigArray[i][cell] in "01234X"):
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

# for i in range(0,len(bigArray)):
#     for j in range(0,len(bigArray[i])):
#         print(bigArray[i][j], end="")
#     print()

for i in range(0, len(bigArray)):
    for j in range(0, len(bigArray[i])):
        if(bigArray[i][j] == "."):
            print(i,j)
            invalid = True
            break
        elif(bigArray[i][j] == "B"):
            viCount += 1
        elif(bigArray[i][j] != "*" and bigArray[i][j] != "L" and bigArray[i][j] != "X"):
            viCount += verifyNumbers(i,j,bigArray)
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
