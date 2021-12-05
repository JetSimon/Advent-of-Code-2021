import itertools, re

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out

def solve_1():
    data = loadData()
    plot = {}
    for inst in data:
        a = inst.split(" -> ")[0].split(",")
        a = [int(n) for n in a]
        b = inst.split(" -> ")[1].split(",")
        b = [int(n) for n in b]

        if(a[0] == b[0] or a[1] == b[1]):
            pos = a
            while True:
                #print(pos)
                posTuple = (pos[0], pos[1])
                dx = 1 if a[0] < b[0] else -1
                if(a[0] == b[0]):
                    dx = 0

                dy = 1 if a[1] < b[1] else -1
                if(a[1] == b[1]):
                    dy = 0

                if posTuple not in plot:
                    plot[posTuple] = 1
                else:
                    plot[posTuple] += 1
                if(pos == b):
                    break
                pos[0] += dx
                pos[1] += dy
    overlap = 0
    for key in plot:
        if plot[key] > 1:
            overlap += 1
    return overlap
        
            
def solve_2():
    data = loadData()
    plot = {}
    for inst in data:
        a = inst.split(" -> ")[0].split(",")
        a = [int(n) for n in a]
        b = inst.split(" -> ")[1].split(",")
        b = [int(n) for n in b]

        pos = a
        while True:
            #print(pos)
            posTuple = (pos[0], pos[1])
            dx = 1 if a[0] < b[0] else -1
            if(a[0] == b[0]):
                dx = 0

            dy = 1 if a[1] < b[1] else -1
            if(a[1] == b[1]):
                dy = 0

            if posTuple not in plot:
                plot[posTuple] = 1
            else:
                plot[posTuple] += 1
            if(pos == b):
                break
            pos[0] += dx
            pos[1] += dy
    overlap = 0
    for key in plot:
        if plot[key] > 1:
            overlap += 1
    return overlap

print("Part 1:", solve_1())

print("Part 2:", solve_2())