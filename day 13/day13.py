import itertools, re

def loadData():
    f = open('input.txt')
    pos = []
    folds = []
    onFolds = False

    for line in f:
        line = line.strip()

        if line == "":
            onFolds = True
            continue

        if not onFolds:
            lineData = line.split(",")
            x = int(lineData[0])
            y = int(lineData[1])
            pos.append( (x,y) )
        else:
            lineData = line.split("fold along ")[1].split("=")
            folds.append( (lineData[0], int(lineData[1])) )

    f.close()
    return pos, folds

def getDim(sheet):
    maxX = 0
    maxY = 0
    for pos in sheet:
        maxX = max(pos[0],maxX)
        maxY = max(pos[1],maxY)
    return maxX, maxY

def printSheet(sheet):
    X,Y = getDim(sheet)
    
    for y in range(Y):
        s = ""
        for x in range(X):
            if (x,y) in sheet:
                s += "#"
            else:
                s += "."
        print(s)
    print("\n")


def solve_1():
    positions, folds = loadData()
    
    sheet = {}
    for pos in positions:
        sheet[(pos[0],pos[1])] = True
    
    for inst in folds:
        maxX, maxY = getDim(sheet)
        print(maxX,maxY)
        nextSheet = {}
        line = inst[1]
        if inst[0] == "x":
            for pos in sheet:
                x = pos[0]
                y = pos[1]
                extra = 0 if maxX % line == 0 else 1
                if x > line:
                    x = maxX - x + extra
                nextSheet[(x,y)] = True
        elif inst[0] == "y":
             for pos in sheet:
                x = pos[0]
                y = pos[1]
                extra = 0 if maxY % line == 0 else 1
                if y > line:
                    y = maxY - y + extra
                nextSheet[(x,y)] = True
        sheet = nextSheet
    
    return len(sheet)

def solve_2():
    positions, folds = loadData()
    
    sheet = {}
    for pos in positions:
        sheet[(pos[0],pos[1])] = True
    
    for inst in folds:
        maxX, maxY = getDim(sheet)
        #print(maxX,maxY)
        nextSheet = {}
        line = inst[1]
        if inst[0] == "x":
            for pos in sheet:
                x = pos[0]
                y = pos[1]
                extra = 0 if maxX % line == 0 else 1
                if x > line:
                    x = maxX - x + extra
                nextSheet[(x,y)] = True
        elif inst[0] == "y":
             for pos in sheet:
                x = pos[0]
                y = pos[1]
                extra = 0 if maxY % line == 0 else 1
                if y > line:
                    y = maxY - y
                nextSheet[(x,y)] = True
        sheet = nextSheet
    
        printSheet(sheet)

print("Part 1:", solve_1())

print("Part 2:", solve_2())