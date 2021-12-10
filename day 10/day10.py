import itertools, re

pairs = {
        "(":")",
        "[":"]",
        "{":"}",
        "<":">"
        }

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out


def solve_1():
    scores = {
        ")":3,
        "]":57,
        "}":1197,
        ">":25137
        }
    score = 0
    data = loadData()
    for line in data:
        stack = []
        valid = True
        for c in line:
            if c in pairs.keys():
                stack.append(c)
            elif c in pairs.values():
                if c == pairs[stack[-1]]:
                    #print(c,"matches",stack[-1])
                    stack.pop()
                else:
                    #print("stopping at", c, stack)
                    score += scores[c]
                    valid = False
                    break
    return score


def solve_2():
    scores = {
        ")":1,
        "]":2,
        "}":3,
        ">":4
        }
    score = []
    data = loadData()
    for line in data:
        stack = []
        valid = True
        for c in line:
            if c in pairs.keys():
                stack.append(c)
            elif c in pairs.values():
                if c == pairs[stack[-1]]:
                    #print(c,"matches",stack[-1])
                    stack.pop()
                else:
                    valid = False
                    break
        if valid:
            stack.reverse()
            s = 0
            for c in stack:
                s *= 5
                s += scores[pairs[c]]
            score.append(s)
    score.sort()
    return score[int(len(score)/2)]


print("Part 1:", solve_1())

print("Part 2:", solve_2())