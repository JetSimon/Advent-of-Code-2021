import itertools, re

def solve_1():

    count = 0
    vRange = 500
    minX = 81
    maxX = 129
    minY = -150
    maxY = -108
    alphaY = 0

    for ivy in range(vRange):
        for ivx in range(vRange):
            enteredTarget = False
            vy = ivy
            vx = ivx
            count += 1
            x = 0
            y = 0
            bestY = 0
            while y > minY and x < maxX:
                x += vx
                y += vy
                bestY = max(y, bestY)

                if vx != 0:
                    vx += 1 if vx < 0 else -1
                
                vy -= 1

                if x >= minX and x <= maxX and y >= minY and y <= maxY:
                    #print(x,y,"entered with velocity",vx,vy, "initial of",ivx,ivy,"best y",bestY)
                    enteredTarget = True

            if(count % 100000 == 0):
                print(count, "/", 4*vRange*vRange)

            if enteredTarget:
                if bestY > alphaY:
                    alphaY = bestY
                    #print("new best", alphaY)

    return alphaY

def solve_2():
    count = 0
    vRange = 500
    minX = 81
    maxX = 129
    minY = -150
    maxY = -108
    solutions = 0

    for ivy in range(-vRange,vRange):
        for ivx in range(vRange):
            vy = ivy
            vx = ivx
            count += 1
            x = 0
            y = 0
            bestY = 0
            while y > minY and x < maxX:
                x += vx
                y += vy
                bestY = max(y, bestY)

                if vx != 0:
                    vx += 1 if vx < 0 else -1
                
                vy -= 1

                if x >= minX and x <= maxX and y >= minY and y <= maxY:
                    solutions += 1
                    break

            if(count % 100000 == 0):
                print(count, "/", 4*vRange*vRange)


    return solutions

print("Part 1:", solve_1())

print("Part 2:", solve_2())