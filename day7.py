class Dir:
    def __init__(self, name, parentDir = None):
        self.name = name
        self.fileList = []
        self.parentDir = parentDir
        self.size = 0

    def addFile(self, item):
        self.fileList.append(item)

    def st(self, level=0):
        ret = "  " * level + str(self.name) + " " + str(self.size) + "\n"
        for child in self.fileList:
            ret += child.st(level+1)
        return ret

    def openDir(self, name):
        for i in self.fileList:
            if i.name == name:
                return i
            
    def __str__(self):
        for i in self.fileList:
            print(i.name)

    
def createDir():
    with open(r"C:\Users\carte\OneDrive\Desktop\High School Code\Nonlinear Dynamics\AdventOfCode2022\day7.txt") as f:
        data = f.readlines()
        topDir = currDir = Dir("/")
        for item in data[1:]:
            item = item[0:-1]
            if item[0:1] == "$":
                if item[2:4] == "cd":
                    if item[5:7] == "..":
                        currDir = currDir.parentDir
                    else:
                        currDir = currDir.openDir(item[5::])
            else:
                if item[0:3] == "dir":
                    currDir.addFile(Dir(item[4::], currDir))
                else:
                    fileVal = item.partition(" ")[0]
                    # Size is size of files in current Directory not Sub Directory
                    currDir.size += int(fileVal)
        return topDir

topDir = createDir()

# Returns Total Size of DIR including sub DIR
def getSize(dir):
    ret = dir.size
    for child in dir.fileList:
        ret += getSize(child)
    return ret

def searchDir(dir):
    if dir.fileList == []:
        temp = getSize(dir)
        if temp <= 100000:
            return temp
        else:
            return 0
    else:
        temp = getSize(dir)
        hold = 0
        if temp <= 100000:
            for child in dir.fileList:
                hold += searchDir(child)
            hold += temp
        else:
            for child in dir.fileList:
                hold += searchDir(child)
        return hold

print(getSize(topDir))
print(searchDir(topDir))
        






