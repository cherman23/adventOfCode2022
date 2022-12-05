def prob1():
    # Create a list of lists containg each of the letters 
    # when its asks to move them, just get tat first section of the list 
    # it might work as well as strings 
        # just add them to the top 

    # remember decrement the indeces from the files by one
    # because python lists start with one 
    # manually create the list of letters

    # each crate is moved one at a time 
    # so when its moved do it in a loop not as a chunk 
    # or you could do it as a chunk but you have to reverse the string first 
    # honestly this problem is kinda simple 

    # to get the numbers use the find() method on the words 
        # dont forget that there is spaces

    with open(r"C:\Users\carte\OneDrive\Desktop\Nonlinear Dynamics\AdventOfCode2022\day5.txt") as f:
        data = f.readlines()

        strList = ["FRW","PWVDCMHT","LNZMP","RHCJ","BTQHGPC","ZFLWCG","CGJZQLVW","CVTWFRNP","VSRGHWJ"]

        for line in data:

            fromIndex = line.find("from")
            toIndex = line.find("to")

            amountNum = int(line[5:fromIndex-1])

            # decrement these because of python listing
            originNum = int(line[fromIndex+5:toIndex-1])-1
            destinationNum = int(line[toIndex+3:len(line)])-1

            # get the string 
            temp = strList[originNum]
            # get the section of the string 
            movingStr = temp[0:amountNum]

            # THIS IS COMMENTED OUT FOR PART 2
            # IF YOU WANT IT FOR PART ONE UNCOMMENT IT 
            #movingStr = movingStr[::-1]
            
            # edit the original section of the list 
            # its everything after the original num
            strList[originNum] = temp[amountNum:len(temp)]
            

            # Add it to the other section
            strList[destinationNum] = movingStr + strList[destinationNum]

        print(strList)
            

prob1()
