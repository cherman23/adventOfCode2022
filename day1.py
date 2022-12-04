def main():
    calMax = 0
    n = 0

    with open(r'C:\Users\carte\OneDrive\Desktop\Nonlinear Dynamics\AdventOfCode2022\day1.txt') as f:
       # for line in f:
       #     print(line.strip())
       data = f.readlines()

       
       for i in data:
        if i != "\n":
            n+= int(i)
        else:
            if calMax < n:
                calMax = n
            n = 0
    
    print(calMax)

def main2():
    calList = []
    n = 0

    with open(r'C:\Users\carte\OneDrive\Desktop\Nonlinear Dynamics\AdventOfCode2022\day1.txt') as f:
       # for line in f:
       #     print(line.strip())
       data = f.readlines()
 
       
       for i in data:
        if i != "\n":
            n+= int(i)
        else:
            calList.append(n)
            n = 0
    
    result = 0

    for i in range(3):
        result += max(calList)
        calList.remove( max(calList))
    
    print(result)

main2()
