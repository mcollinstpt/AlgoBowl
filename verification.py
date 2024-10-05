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

def findLitLight(i,j,bigArray,viCount):
    print("TODO: write verifyNumbers")

def verifyNumbers(i,j,bigArray,viCount):
    print("TODO: write verifyNumbers")

bigArray = []
with open("input_backup.txt") as input:
    violations = int(input.readline().replace("\n",""))

    for line in input:
        bigArray.append(list(line.replace("\n","")))

viCount = 0

for i in range(0, len(bigArray)):
    for j in range(0, len(bigArray[i])):
        if(bigArray[i][j] == "L"):
            changeToBulb(i,j,bigArray)
            findLitLight()

invalid = False

for i in range(0, len(bigArray)):
    for j in range(0, len(bigArray[i])):
        if(bigArray[i][j] == "."):
            invalid = True
            break
        elif(bigArray[i][j] == "B"):
            viCount += 1
        elif(bigArray[i][j] != "*" and bigArray[i][j] != "L" and bigArray[i][j] != "X"):
            verifyNumbers(i,j,bigArray)
    if(invalid):
        break

if(viCount != violations or invalid):
    print("INVALID      WRONG       BAD")

else:
    print("VALID    CORRECT     GOOD")
