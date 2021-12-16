import itertools, re

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out

def hexToBin(hex):
    d = {"0":"0000", "1":"0001", "2":"0010", "3":"0011",
    "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000",
    "9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
    out = ""
    for c in hex:
        out += d[c]
    return out

def decodeNormalPacket(s):
    length = 6
    data = ""
    for i in range(6, len(s), 5):
        length += 5
        data += s[i+1:i+5]
        if s[i] == "0":
            break
    data = int(data, 2)
    return data, length

def decode(s, versions):
    currentPos = 0
    version = int(s[:3],2)
    
    versions[0] += version
    id = int(s[3:6],2)

    if id == 4:
        data, length = decodeNormalPacket(s)
      
      #  print("packet has version", version, "id of",id, "data is",data,"length of",length)
        return data, currentPos + length
    else:
        currentPos += 7
        lid = s[6]
      #  print(s,"is operator version", version,"lid of",lid)
        packets = []
        if lid == "0":
            lenAmt = 15
            length = s[7:7+lenAmt]
            currentPos += lenAmt
            length = int(length,2)
           # print("has length of ",length)
            currentLength = 0
            nextParse = s[currentPos:]
            while currentLength < length:
                data, offset = decode(nextParse, versions)
                currentLength += offset
                currentPos += offset
                nextParse = s[currentPos:]
                packets.append(data)
           # print("ended at pos", currentPos)
        elif lid == "1":
            lenAmt = 11
            numOfPackets = s[7:7+lenAmt]
            numOfPackets = int(numOfPackets,2)
            currentPos += lenAmt
            #print("has ",numOfPackets,"packets")
            nextParse = s[currentPos:]
            for p in range(numOfPackets):
                data, offset = decode(nextParse, versions)
                currentPos += offset
                nextParse = s[currentPos:]
                packets.append(data)
           # print(packets)

        

        return packets, currentPos

def mul(arr):
    out = 1
    for e in arr:
        out *= e
    return out


def decode2(s, versions):
    currentPos = 0
    version = int(s[:3],2)
    id = int(s[3:6],2)

    if id == 4:
        data, length = decodeNormalPacket(s)
        #print("packet has version", version, "id of",id, "data is",data,"length of",length)
        return data, currentPos + length
    else:
        currentPos += 7
        lid = s[6]
       # print(s,"is operator version", version,"lid of",lid)
        packets = []
        if lid == "0":
            lenAmt = 15
            length = s[7:7+lenAmt]
            currentPos += lenAmt
            length = int(length,2)
           # print("has length of ",length)
            currentLength = 0
            nextParse = s[currentPos:]
            while currentLength < length:
                data, offset = decode2(nextParse, versions)
                currentLength += offset
                currentPos += offset
                nextParse = s[currentPos:]
                packets.append(data)
           # print("ended at pos", currentPos)
        elif lid == "1":
            lenAmt = 11
            numOfPackets = s[7:7+lenAmt]
            numOfPackets = int(numOfPackets,2)
            currentPos += lenAmt
            #print("has ",numOfPackets,"packets")
            nextParse = s[currentPos:]
            for p in range(numOfPackets):
                data, offset = decode2(nextParse, versions)
                currentPos += offset
                nextParse = s[currentPos:]
                packets.append(data)

        if id == 0:
            packets = sum(packets)
        elif id == 1:
            packets = mul(packets)
        elif id == 2:
            packets = min(packets)
        elif id == 3:
            packets = max(packets)
        elif id == 5:
            packets = 1 if packets[0] > packets[1] else 0
        elif id == 6:
            packets = 1 if packets[0] < packets[1] else 0
        elif id == 7:
            packets = 1 if packets[0] == packets[1] else 0

        return packets, currentPos



def solve_1():
    data = loadData()
    versions = [0]
    for code in data:
        decode(hexToBin(code), versions)
    return versions

def solve_2():
    data = loadData()
    for code in data:
        result,_=decode2(hexToBin(code), [])
    return result

print("Part 1:", solve_1())

print("Part 2:", solve_2())