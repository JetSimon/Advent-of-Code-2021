import itertools, re
from copy import deepcopy

def loadData():
    f = open('input.txt')
    out = []
    for line in f:
        row = list(line.strip())
        row = [int(n) for n in row]
        out.append(row)
    f.close()
    return out

def validPos(arr, y, x):
    valid = y >= 0 and y < len(arr) and x >= 0 and x < len(arr[y])
    return valid

def printBoard(arr):
    for line in arr:
        print(line)

def solve_1():
    data = loadData()
    steps = 100
    flashes = 0

    for step in range(steps):
        next = deepcopy(data)
        #print("STEP",step)
        #printBoard(data)
        #print("\n")
        flashed = {}

        for y in range(len(data)):
            for x in range(len(data[y])):
                next[y][x] += 1
        
        someoneFlashed = True
        while someoneFlashed:
            nextFlash = deepcopy(next)
            someoneFlashed = False
            for y in range(len(next)):
                for x in range(len(next[y])):
                    if(next[y][x] > 9 and (y,x) not in flashed):
                        someoneFlashed = True
                        flashed[(y,x)] = True
                        flashes += 1
                        for dy in range(-1,2):
                            for dx in range(-1,2):
                                if (dy == 0 and dx == 0) or not validPos(nextFlash,y+dy,x+dx):
                                    continue
                                nextFlash[y+dy][x+dx] += 1
            next = nextFlash

        for key in flashed:
            next[key[0]][key[1]] = 0
        
        data = next

    return flashes

def solve_2():
    data = loadData()
    step = 0
    while True:
        next = deepcopy(data)
        print("STEP",step)
        #printBoard(data)
        #print("\n")
        flashed = {}

        for y in range(len(data)):
            for x in range(len(data[y])):
                next[y][x] += 1
        
        someoneFlashed = True
        while someoneFlashed:
            nextFlash = deepcopy(next)
            someoneFlashed = False
            for y in range(len(next)):
                for x in range(len(next[y])):
                    if(next[y][x] > 9 and (y,x) not in flashed):
                        someoneFlashed = True
                        flashed[(y,x)] = True
                        for dy in range(-1,2):
                            for dx in range(-1,2):
                                if (dy == 0 and dx == 0) or not validPos(nextFlash,y+dy,x+dx):
                                    continue
                                nextFlash[y+dy][x+dx] += 1
            next = nextFlash

        for key in flashed:
            next[key[0]][key[1]] = 0
        
        data = next

        step += 1

        if len(flashed) == 100:
            break
        


    return step

print("Part 1:", solve_1())

print("Part 2:", solve_2())