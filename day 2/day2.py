import itertools, re

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out

data = loadData()

def solve_1(data):
    pos = 0
    depth = 0
    for inst in data:
        raw = inst.split(" ")
        direction = raw[0]
        amt=  int(raw[1])
        if(direction == "forward"):
            pos += amt
        elif(direction == "down"):
            depth += amt
        elif(direction == "up"):
            depth -= amt
    return pos * depth

def solve_2(data):
    pos = 0
    depth = 0
    aim = 0
    for inst in data:
        raw = inst.split(" ")
        direction = raw[0]
        amt=  int(raw[1])
        if(direction == "forward"):
            pos += amt
            depth += amt * aim
        elif(direction == "down"):
            aim += amt
        elif(direction == "up"):
            aim -= amt
    return pos * depth

print("Part 1:", solve_1(data))

print("Part 2:", solve_2(data))