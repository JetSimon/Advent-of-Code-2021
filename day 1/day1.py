import itertools, re

def loadData():
    f = open('input.txt')
    out = [int(line.strip()) for line in f]
    f.close()
    return out

data = loadData()

def solve_1(data):
    bigger = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            bigger += 1
    return bigger

def solve_2(data):
    bigger = 0
    for i in range(1, len(data)-2):
        if data[i] + data[i+1] + data[i+2] > data[i-1] + data[i] + data[i+1]:
            bigger += 1
    return bigger

print(solve_2(data))