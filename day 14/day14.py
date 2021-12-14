import itertools, re

def loadData():
    f = open('input.txt')
    seed = None
    rules = {}

    for line in f:
        if not seed:
            seed = line.strip()
        else:
            line = line.strip()
            if line != "":
                a = line.split(" -> ")[0]
                b = line.split(" -> ")[1]
                rules[a] = b

    f.close()
    return seed, rules

def mostLeast(arr):
    most = 0
    least = len(arr)
    for e in set(arr):
        c = arr.count(e)
        if c > most:
            most = c
        if c < least:
            least = c
    return most - least

def mostLeastDict(d):
    return max(d.values()) - min(d.values())

def getCounts(arr):
    counts = {}
    for e in set(arr):
        c = arr.count(e)
        counts[e] = c
    return counts

def solve_1():
    steps = 10
    seed, rules = loadData()
    for step in range(steps):
        #print(step)
        nextSeed = list(seed)
        offset = 0
        for i in range(len(seed)-1):
            pair = seed[i] + seed[i+1]
            if pair in rules:
                nextSeed.insert(i+1+offset,rules[pair])
                offset += len(rules[pair])
        seed = "".join(nextSeed)
    return mostLeast(list(seed))

def getPairs(seed):
    pairs = {}
    for i in range(len(seed)-1):
        pair = seed[i] + seed[i+1]
        if pair not in pairs:
            pairs[pair] = 1
        else:
            pairs[pair] += 1
    return pairs

def solve_2():
    steps = 40
    seed, rules = loadData()
    pairs = getPairs(seed)
    counts = getCounts(seed)

    for step in range(steps):
        #print("step", step, ":", counts, "pairs:",pairs)
        nextPairs = {}

        for pair in pairs:
            if pair in rules:
                multi = pairs[pair]

                a = pair[0] + rules[pair]
                b = rules[pair] + pair[1]

                #print(a,b)
                
                counts[rules[pair]] = multi if rules[pair] not in counts else counts[rules[pair]] + multi
                #counts[pair[0]] = 1 if pair[0] not in counts else counts[pair[0]] + 1
                #counts[pair[1]] = 1 if pair[1] not in counts else counts[pair[1]] + 1

                #print(a,b)

                if a not in nextPairs:
                    nextPairs[a] = multi
                else:
                    nextPairs[a] += multi

                if b not in nextPairs:
                    nextPairs[b] = multi
                else:
                    nextPairs[b] += multi
                
        pairs = nextPairs

    return mostLeastDict(counts)


print("Part 1:", solve_1())

print("Part 2:", solve_2())