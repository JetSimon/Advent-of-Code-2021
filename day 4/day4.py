import itertools, re
from copy import deepcopy
def loadData():
    f = open('input.txt')
    numbersFound = False
    nums = []
    boards = []
    currentBoard = []
    for line in f:
        line = line.strip()
        if not numbersFound:
            nums = line.split(",")
            nums = [int(n) for n in nums]
            numbersFound = True
        else:
            if(line == ""):
                if(currentBoard != []):
                    boards.append(currentBoard)
                    currentBoard = []
            else:
                l = line.replace("  ", " ").strip().split(" ")
                l = [int(n) for n in l]
                currentBoard.append(l)
    if currentBoard != []:
        boards.append(currentBoard) 

    f.close()
    return (nums, boards)

def printBoard(board):
    for line in board:
        print(line)
    print("\n")

def checkBoard(board):
    for row in board:
        if(set(row) == {'X'}):
            return True
    for col in range(len(board[0])):
        winner = True
        for row in range(len(board)):
            if(board[row][col] != "X"):
                winner = False
                break
        if winner:
            return True
    return False
        
def sumBoard(board):
    s = 0
    for line in board:
        for n in line:
            if(n != "X"):
                s += n
    return s

def findNumAndReplace(board, num):
    for line in board:
        for i in range(len(line)):
            n = line[i]
            if(n == num):
                line[i] = "X"
    

def solve_1():
    nums, boards = loadData()
    winner = None
    lastCalled = None
    for num in nums:
        lastCalled = num
        for board in boards:
            findNumAndReplace(board, num)
            if checkBoard(board):
                winner = board
                break
        #print("num:",num)
        #printBoard(boards[2])
        if winner != None:
            break
    #printBoard(winner)
    #print("last called:",lastCalled)
    return sumBoard(winner) * lastCalled
        
def solve_2():
    nums, boards = loadData()
    wonIndex = {}
    lastWon = None
    lastCalled = None
    for num in nums:
        #print(num)
        
        for i in range (len(boards)):
            if i not in wonIndex:
                board = boards[i]
                findNumAndReplace(board, num)
                if checkBoard(board):
                    lastCalled = num
                    print("winner")
                    lastWon = board
                    wonIndex[i] = True
     
    print("last called:",lastCalled)
    return sumBoard(lastWon) * lastCalled

print("Part 1:", solve_1())

print("Part 2:", solve_2())