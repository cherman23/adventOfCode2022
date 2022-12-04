def prob1():
    priorityPoints = 0
    letterDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
    'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26, 'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,
    'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52}

    with open(r"C:\Users\carte\OneDrive\Desktop\Nonlinear Dynamics\AdventOfCode2022\day3.txt") as f:
        data = f.readlines()

        for line in data:
            line = line[0:len(line)-1]
            x = int(len(line)/2)
            stopWord = False
            
            firstHalf  = line[0:x]
           # print(len(firstHalf))
            secondHalf = line[x:len(line)]
          #  print(len(secondHalf))

            for char in firstHalf:
                for j in secondHalf:
                    if letterDict[char] == letterDict[j]:
                        print(char)
                        priorityPoints += letterDict[char]
                        stopWord = True
                        break
                if stopWord == True:
                    break

    print(priorityPoints)

def prob2():
    priorityPoints = 0
    letterDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
    'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26, 'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,
    'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52}

    with open(r"C:\Users\carte\OneDrive\Desktop\Nonlinear Dynamics\AdventOfCode2022\day3.txt") as f:
        data = f.readlines()
        print(len(data)/3)
        i = 0

        while i < len(data)-2:
            groupOne = data[i]
            groupTwo = data[i+1]
            groupThree = data[i+2]
            
            stopWord = False

            for char in groupOne:
                for j in groupTwo:
                    for k in groupThree:
                        if char != '\n' and j != '\n' and k != '\n': 
                            if letterDict[char] == letterDict[j] and letterDict[char] == letterDict[k]:
                                priorityPoints += letterDict[char]
                                stopWord = True
                                break
                    if stopWord == True:
                        break
                if stopWord == True:
                    break
            i+=3
                    
    print(priorityPoints)

prob2()
