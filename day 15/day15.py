import itertools, re
from math import inf
import math

def loadData():
    f = open('input.txt')
    out = [[int(n) for n in list(line.strip())] for line in f]

    f.close()
    return out

def validPos(grid,x,y):
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def findLeastRes(grid):
    x = 0
    y = 0
    risk = 0
    while x != len(grid[0]) - 1 or y != len(grid) - 1:
       
        a = None if not validPos(grid,x+1,y) else grid[y][x+1]
        b = None if not validPos(grid,x,y+1) else grid[y+1][x]
        
        print(x,y,a,b)
        
        if b == None:
            x += 1
        elif a == None:
            y += 1
        elif a == b or b < a:
            y += 1
        elif a < b:
            x += 1
        risk += grid[y][x]
    
    print("done at", x,y)

    return risk

def createSet(grid, default):
    out = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            out[(x,y)] = default
    return out

def createQueue(grid):
    out = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            out.append((x,y))
    return out

def distToEnd(point,end):
    return math.sqrt(((point[0] - end[0]) ** 2) + ((point[1] - end[1]) ** 2))

def getNextTo(grid, pos):
    x = pos[0]
    y = pos[1]
    choices = [(x,y+1), (x-1,y), (x+1,y), (x,y-1)]
    out = []
    for choice in choices:
        if validPos(grid, choice[0], choice[1]):
            out.append(choice)
    return out 

def getClosest(grid, current, onPath, end):
    x = current[0]
    y = current[1]
    choices = [(x,y+1), (x-1,y), (x+1,y), (x,y-1)]
    out = []
    for choice in choices:
        if validPos(grid, choice[0], choice[1]) and choice not in onPath:
            out.append(choice)
    best = None
    for choice in out:
        if best == None or grid[choice[1]][choice[0]] + distToEnd(choice,end) < grid[best[1]][best[0]] + distToEnd(choice,end):
            best = choice

    return best

def solve_1():
    grid = loadData()
    risks = loadData()

    start = (0,0)
    end = (len(grid[0])-1,len(grid)-1)

    costs = createSet(grid, inf)
    costs[start] = 0
    queue = [start]

    searched = set()
    total = len(grid[0]) * len(grid)

    while queue:
        current = queue.pop(0)
        searched.add(current)
        #print(len(searched),"/",total)

        for node in getNextTo(grid, current):
            a = costs[node]
            b = costs[current] + risks[node[0]][node[1]]
            if a > b:
                costs[node] = b
                queue.append(node)
    
    return costs[end]


def getBigGrid():
    orig = loadData()
    height = len(orig)
    width = len(orig[0])
    out = []
    for y in range(height * 5):
        row = []
        for x in range(width * 5):
            xOffSet = math.floor(x / width)
            yOffSet = math.floor(y / height)
            val = (orig[y % height][x % height] + xOffSet + yOffSet)
            newVal = math.floor((val % 10) + (val/10))
            row.append(newVal)
        out.append(row)

    return out

def solve_2():
    grid = getBigGrid()
    risks = grid[:]

    start = (0,0)
    end = (len(grid[0])-1,len(grid)-1)

    costs = createSet(grid, inf)
    costs[start] = 0
    queue = [start]

    searched = set()
    total = len(grid[0]) * len(grid)

    while queue:
        current = queue.pop(0)
        searched.add(current)
        print(len(searched),"/",total)

        for node in getNextTo(grid, current):
            a = costs[node]
            b = costs[current] + risks[node[0]][node[1]]
            if a > b:
                costs[node] = b
                queue.append(node)
    
    return costs[end]


print("Part 1:", solve_1())

print("Part 2:", solve_2())