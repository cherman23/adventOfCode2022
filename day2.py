def prob1():
    pointDict = {"X":1, "Y":2, "Z":3, "A":1, "B":2, "C":3}
    outcomeDict = {"Loss": 0, "Draw": 3, "Win": 6}
    pointTotal = 0

    with open(r"C:\Users\carte\OneDrive\Desktop\Nonlinear Dynamics\AdventOfCode2022\day2.txt") as f:
        data = f.readlines()

        for line in data:
            line.replace("\n","") 

            input1 = line[0:1]
            input2 = line[2:3]
            pointTotal += pointDict[input2]

            # Check for draw
            if pointDict[input2] == pointDict[input1]:
                pointTotal+=outcomeDict["Draw"]

            # Check for win
            elif input1 == "A" and input2 == 'Y':
                pointTotal+=outcomeDict["Win"]

            elif input1 == "A" and input2 == 'Z':
                pointTotal+=outcomeDict["Loss"]

            elif input1 == "B" and input2 == 'X':
                pointTotal+=outcomeDict["Loss"]

            elif input1 == "B" and input2 == 'Z':
                pointTotal+=outcomeDict["Win"]

            elif input1 == "C" and input2 == 'X':
                pointTotal+=outcomeDict["Win"]

            elif input1 == "C" and input2 == 'Y':
                pointTotal+=outcomeDict["Loss"]

    print(pointTotal)

def prob2():
    pointTotal = 0
    outcomeDict = {"X": 0, "Y": 3, "Z": 6}

    with open(r"C:\Users\carte\OneDrive\Desktop\Nonlinear Dynamics\AdventOfCode2022\day2.txt") as f:
        data = f.readlines()

        for line in data:
            otherInput = line[0:1]
            myInput = line[2:3]

            pointTotal+=outcomeDict[myInput]

            # supposed to win
            if myInput == "Z":
                if otherInput == "A":
                    pointTotal+=2
                if otherInput == "B":
                    pointTotal+=3
                if otherInput == "C":
                    pointTotal+=1
            #supposed to tie
            elif myInput == "Y":
                if otherInput == "A":
                    pointTotal+=1
                if otherInput == "B":
                    pointTotal+=2
                if otherInput == "C":
                    pointTotal+=3
            #supposed to lose 
            elif myInput == "X":
                if otherInput == "A":
                    pointTotal+=3
                if otherInput == "B":
                    pointTotal+=1
                if otherInput == "C":
                    pointTotal+=2

    print(pointTotal)

prob2()

