import itertools, re

def loadData():
    f = open('input.txt')
    out = []
    for line in f:
        row = list(line.strip())
        row = [int(n) for n in row]
        out.append(row)
    f.close()
    return out

def getNeighbours(arr, y, x):
    neighbours = []
    if y + 1 < len(arr):
        neighbours.append(arr[y+1][x])
    if y - 1 >= 0:
        neighbours.append(arr[y-1][x])
    if x + 1 < len(arr[y]):
        neighbours.append(arr[y][x+1])
    if x - 1 >= 0:
        neighbours.append(arr[y][x-1])
    return neighbours
    

def solve_1():
    data = loadData()
    totalRisk = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            e = data[y][x]
            n = getNeighbours(data, y, x)
            lowest = True
            for i in n:
                if i <= e:
                    lowest = False
                    break
            if lowest:
                #print(e, n)
                totalRisk += 1 + e
    return totalRisk 

def floodFill(arr, y, x, count):
    if(arr[y][x] == 9 or arr[y][x] == "X"):
        return
    
    count[0] += 1
    arr[y][x] = "X"
    
    if y + 1 < len(arr):
        floodFill(arr, y+1, x,count)
    if y - 1 >= 0:
        floodFill(arr, y-1, x,count)
    if x + 1 < len(arr[y]):
        floodFill(arr, y, x+1,count)
    if x - 1 >= 0:
        floodFill(arr, y, x-1,count)

def printBoard(arr):
    for line in arr:
        print(line)

def solve_2():
    data = loadData()
    totals = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            count = [0]
            floodFill(data,y,x,count)
            if(count != 0):
                totals.append(count[0])
    totals.sort()
    return totals[-1] * totals[-2] * totals[-3]


print("Part 1:", solve_1())

print("Part 2:", solve_2())