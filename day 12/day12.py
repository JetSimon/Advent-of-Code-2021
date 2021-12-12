import itertools, re

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out

def isSmall(c):
    return c.islower()

def find(node, nodes, visited, path, count):
    path += f" -> {node}"

    if node == "end":
        #print(path)
        count[0] += 1
        return

    visited = visited[:]
    if isSmall(node):
        visited.append(node)

    for dest in nodes[node]:
        if dest not in visited:
            find(dest, nodes, visited, path, count)

def find2(node, nodes, visited, path, count):
    path += f" -> {node}"

    if node == "end":
        #print(path)
        count[0] += 1
        return

    visited = visited[:]
    if isSmall(node):
        visited.append(node)

    for dest in nodes[node]:
        if dest == "start":
            if dest not in visited:
                find2(dest, nodes, visited, path, count)
        elif len(set(visited)) + 1 >= len(visited):
            find2(dest, nodes, visited, path, count)


def solve_1():
    data = loadData()
    startingNodes = []
    nodes = {}
    count = [0]
    for line in data:
        a = line.split("-")[0]
        b = line.split("-")[1]
        if a == "start":
            startingNodes.append(b)
        elif b == "start":
            startingNodes.append(a)
        else:
            if a not in nodes:
                nodes[a] = [b]
            else:
                nodes[a].append(b)
            
            if b != "end":
                if b not in nodes:
                    nodes[b] = [a]
                else:
                    nodes[b].append(a)

    print(nodes)
    
    for node in startingNodes:
        find(node, nodes, [], "start", count)

    return count[0]

def solve_2():
    data = loadData()
    startingNodes = []
    nodes = {}
    count = [0]
    for line in data:
        a = line.split("-")[0]
        b = line.split("-")[1]
        if a == "start":
            startingNodes.append(b)
        elif b == "start":
            startingNodes.append(a)
        else:
            if a not in nodes:
                nodes[a] = [b]
            else:
                nodes[a].append(b)
            
            if b != "end":
                if b not in nodes:
                    nodes[b] = [a]
                else:
                    nodes[b].append(a)

    #print(nodes)
    
    for node in startingNodes:
        find2(node, nodes, [], "start", count)

    return count[0]



print("Part 1:", solve_1())

print("Part 2:", solve_2())