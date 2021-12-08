import itertools, re

reals = [
    [1,1,1,0,1,1,1], #0
    [0,0,1,0,0,1,0], #1
    [1,0,1,1,1,0,1], #2
    [1,0,1,1,0,1,1], #3
    [0,1,1,1,0,1,0], #4
    [1,1,0,1,0,1,1], #5
    [1,1,0,1,1,1,1], #6
    [1,0,1,0,0,1,0], #7
    [1,1,1,1,1,1,1], #8
    [1,1,1,1,0,1,1]  #9
]

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out

def solve_1(): 
    data = loadData()
    out = 0
    for line in data:
        output = line.split("|")[1].strip().split(" ")
        for code in output:
            if len(code) in [2,4,3,7]:
                #print(code)
                out += 1
    return out

def pushDict(e,val,dict):
    if e in dict:
        if val in dict[e]:
            dict[e][val] += 1
        else:
            dict[e][val] = 1
    else:
        dict[e] = {val:1}

def parseInput(input, segments):
    for code in input:
        l = len(code)
        if l in [2,4,3,7]:
            if l == 2: #is 1
                for val in code:
                    pushDict('c', val, segments)
                    pushDict('f', val, segments)
            elif l == 3: #is 7
                for val in code:
                    pushDict('a', val, segments)
                    pushDict('c', val, segments)
                    pushDict('f', val, segments)
            elif l == 4: #is 4
                for val in code:
                    pushDict('b', val, segments)
                    pushDict('c', val, segments)
                    pushDict('d', val, segments)
                    pushDict('f', val, segments)
            elif l == 7: #is 8
                for val in code:
                    pushDict('a', val, segments)
                    pushDict('b', val, segments)
                    pushDict('c', val, segments)
                    pushDict('d', val, segments)
                    pushDict('e', val, segments)
                    pushDict('f', val, segments)
                    pushDict('g', val, segments)

def mostFreq(d):
    freq = []
    most = max(d.values())
    for key in d:
        if d[key] == most:
            freq.append(key)
    return freq

def siftTies(segments):
    out = {}
    for key in segments:
        freq = mostFreq(segments[key])
        if freq:
            out[key] = freq
    return out

def getPoss(data, code):
    poss = []
    for a in data['a']:
        for b in data['b']:
            if a == b:
                continue
            for c in data['c']:
                if len(set([a,b,c])) != 3:
                    continue
                for d in data['d']:
                    if len(set([a,b,c,d])) != 4:
                        continue
                    for e in data['e']:
                        if len(set([a,b,c,d,e])) != 5:
                            continue
                        for f in data['f']:
                            if len(set([a,b,c,d,e,f])) != 6:
                                continue
                            for g in data['g']:
                                if len(set([a,b,c,d,e,f,g])) == 7:
                                    attempt = [0] * 7 #0000000
                                    
                                    if a in code:
                                        attempt[0] = 1
                                    if b in code:
                                        attempt[1] = 1
                                    if c in code:
                                        attempt[2] = 1
                                    if d in code:
                                        attempt[3] = 1
                                    if e in code:
                                        attempt[4] = 1
                                    if f in code:
                                        attempt[5] = 1
                                    if g in code:
                                        attempt[6] = 1

                                    if attempt in reals:
                                        return attempt
    return poss

def convertPoss(poss):
    return reals.index(poss)

def solve_2():
    data = loadData()
    out = 0
    for line in data:
        temp = ""
        input = line.split("|")[0].strip().split(" ")
        output = line.split("|")[1].strip().split(" ")
        segments = {}
        parseInput(input,segments)
        sifted = siftTies(segments)
        #print(sifted)
        
        #try all options and see which ones make good numbers
        for code in output:
            poss = getPoss(sifted, code)
            temp += str(convertPoss(poss))
        out += int(temp)

    return out

print("Part 1:", solve_1())

print("Part 2:", solve_2())