import itertools, re

def loadData():
    f = open('input.txt')
    out = []
    for line in f:
        out = line.split(",")
        out = [int(n) for n in out]
    f.close()
    return out

def solve_1():
    data = loadData()
    best = None
    bestCost = sum(data)
    for n in range(0,max(data)):
        totalCost = 0
        for e in data:
            cost = abs(e-n)
            totalCost += cost
        if totalCost < bestCost:
            bestCost = totalCost
            best = n
    return (best, "costs", bestCost)

def sumUp(n):
    return n*(n+1)/2

def solve_2():
    data = loadData()
    data = loadData()
    best = None
    bestCost = sum(data) * 10000
    for n in range(0,max(data)):
        totalCost = 0
        for e in data:
            cost = sumUp(abs(e-n))
            totalCost += cost
        if totalCost < bestCost:
            bestCost = totalCost
            best = n
    return (best, "costs", bestCost)


print("Part 1:", solve_1())

print("Part 2:", solve_2())