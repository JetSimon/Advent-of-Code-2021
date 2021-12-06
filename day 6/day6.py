import itertools, re
from math import e, log

def loadData():
    out = None
    f = open('input.txt')
    for line in f:
        out = line.split(",")
        out = [int(n) for n in out]
    f.close()
    return out

class Fish():
    def __init__(self, pool, timer=8):
        self.timer = timer
        self.pool = pool
    def cycle(self):
        self.timer -= 1
        if(self.timer < 0):
            self.timer = 6
            return 1
        return 0

def solve_1():
    data = loadData()
    pool = []
    pool = [Fish(pool,timer=n) for n in data]
    toAdd = 0
    for day in range(18):
        #if(day % 1 == 0):
            #print("day",day,":",len(pool))
        for fish in pool:
            #print(fish.timer)
            toAdd += fish.cycle()
        for i in range(toAdd):
            pool.append(Fish(pool))
        toAdd = 0
    return len(pool)

def solve_2():
    maxDays = 256
    data = {}  
    rawData = loadData()
    total = len(rawData)
    for p in set(rawData):
        data[p] = rawData.count(p)

    for day in range(maxDays):
        #print(total)
        newData = {}
        for fish in data:
            newData[fish-1] = data[fish]
        if 0 in data:
            total += data[0]
            if 8 in newData:
                newData[8] += data[0]
            else:
                newData[8] = data[0]
            if 6 in newData:
                newData[6] += data[0]
            else:
                newData[6] = data[0]
        data = newData


    return total

print("Part 1:", solve_1())

print("Part 2:", solve_2())