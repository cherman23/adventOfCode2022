def prob():
    containNum = 0
    # This for part two
    overlapNum = 0

    with open(r"C:\Users\carte\OneDrive\Desktop\Nonlinear Dynamics\AdventOfCode2022\day4.txt") as f:
        data = f.readlines()

        for line in data:
            # first find dahses and commas for formatting of numbers 
            dashIndexOne = line.find('-')
            #print(dashIndexOne)
            commaIndex = line.find(',')

            # finding the second instance of the dash
            temp = line[dashIndexOne+1:len(line)]
            temp2 = line[0:dashIndexOne+1]
            dashIndexTwo = temp.find('-') + len(temp2)

            
            # First number range
            minOne = int(line[0:dashIndexOne])
            maxOne = int(line[dashIndexOne+1:commaIndex])
            

            # Second number range 
            minTwo = int(line[commaIndex+1:dashIndexTwo])
            maxTwo = int(line[dashIndexTwo+1:len(line)])

            if minOne <= minTwo and maxOne >= maxTwo:
                containNum +=1
            elif minOne >= minTwo and maxOne <= maxTwo:
                containNum+=1

            # PART TWO OF THE PROBLEM
            # Using the range function you can create 
            # list from two values 
            listOne = list(range(minOne,maxOne+1))
            listTwo = list(range(minTwo,maxTwo+1))
            overlap = False
            for i in listOne:
                for j in listTwo:
                    if i == j:
                        overlap = True
                        overlapNum+=1
                        break
                if overlap == True:
                    break
            
        
        print(containNum)
        print(overlapNum)
            

prob()