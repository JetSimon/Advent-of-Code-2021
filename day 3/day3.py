import itertools, re

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out

data = loadData()

def findMostCommon(data):
    bits = {}
    for s in data:
        for i in range(12):
            if i not in bits:
                bits[i] = [s[i]]
            else:
                bits[i].append(s[i])
    
    gamma = ""
    ep = ""

    for key in bits:
        ones = bits[key].count('1')
        zeroes = bits[key].count('0')

        pos = '1' if ones >= zeroes else '0'

        pos2 = '1' if ones < zeroes else '0'

        gamma += pos
        ep += pos2
    
    return gamma, ep

def solve_1(data):
    bits = {}
    for s in data:
        for i in range(len(s)):
            if i not in bits:
                bits[i] = [s[i]]
            else:
                bits[i].append(s[i])
    
    gamma = ""
    ep = ""

    for key in bits:
        ones = bits[key].count('1')
        zeroes = bits[key].count('0')
        pos = '1' if ones > zeroes else '0'
        pos2 = '1' if ones < zeroes else '0'
        gamma += pos
        ep += pos2

    return int(gamma,2) * int(ep,2)


def solve_2(data):
    
    oxy = data[:]
    oxyBL = {}
    co2 = data[:]
    co2BL = {}

    for i in range(12):
        print(len(oxy), len(co2))
        if(len(oxy) > 1):
            gamma,_ = findMostCommon(oxy)
        if(len(co2) > 1):
            _,ep = findMostCommon(co2)
        for s in data:
            if(len(oxy) > 1):
                if s[i] == gamma[i]:
                    if s not in oxy and s not in oxyBL:
                        oxy.append(s)
                else:
                    if s in oxy:
                        oxy.remove(s)
                    oxyBL[s] = True
            if(len(co2) > 1):
                if s[i] == ep[i]:
                    if s not in co2 and s not in co2BL:
                        co2.append(s)
                else:
                    if s in co2:
                        co2.remove(s)
                    co2BL[s] = True

    oxy = "".join(oxy)
    co2 = "".join(co2)
    
    return int(oxy, 2) * int(co2, 2)



print("Part 1:", solve_1(data))

print("Part 2:", solve_2(data))