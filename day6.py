def day6():
    charCount = 4
    valList = []

    with open(r"C:\Users\carte\OneDrive\Desktop\Nonlinear Dynamics\AdventOfCode2022\day6.txt") as f:

        data = f.read()
        
        # scan in chunks of four and check to see if they all have different values 
            # add one every time to the character count
            # use the numerical value of the letters to see if any are equal
        # increment by one until there is a group of four letters that are all different 
            # start the char count at 4 because it is always necesarry to check the first four chars

        for i in range(len(data)-3):
            valList.append(data[i])
            valList.append(data[i+1])
            valList.append(data[i+2])
            valList.append(data[i+3])
            
            if len(set(valList)) == len(valList):
                 return charCount
            else:
                charCount+=1
                valList = []

def day6Part2():
    charCount = 14
    valList = []

    with open(r"C:\Users\carte\OneDrive\Desktop\Nonlinear Dynamics\AdventOfCode2022\day6.txt") as f:

        data = f.read()
        
        # scan in chunks of fourteen and check to see if they all have different values 
            # add one every time to the character count
            # use the numerical value of the letters to see if any are equal
        # increment by one until there is a group of four letters that are all different 
            # start the char count at 14 because it is always necesarry to check the first four chars

        for i in range(len(data)-13):
            valList.append(data[i])
            valList.append(data[i+1])
            valList.append(data[i+2])
            valList.append(data[i+3])
            valList.append(data[i+4])
            valList.append(data[i+5])
            valList.append(data[i+6])
            valList.append(data[i+7])
            valList.append(data[i+8])
            valList.append(data[i+9])
            valList.append(data[i+10])
            valList.append(data[i+11])
            valList.append(data[i+12])
            valList.append(data[i+13])
            
            if len(set(valList)) == len(valList):
                return charCount
            else:
                charCount+=1
                valList = []



print(day6Part2())
            