import os
import sys
from math import sqrt


sq2 = sqrt(2)

def readFile():
    boardFile = 'board.dat'  # board file

    n = None  # board dimensions
    board = []  # represents the board

    try:
        with open(os.getcwd() + '\\' + boardFile) as currentFile:
            n = int(currentFile.readline().strip())

            for i in range(n):
                row = [float(x) for x in currentFile.readline().strip().split()]  # read the board row-by-row

                board.insert(i, row)

        currentFile.close()

    except FileNotFoundError:
        print('ERROR: File', boardFile, 'not found.')
        sys.exit()

    except Exception as e:
        print(e)
        sys.exit()

    return n, board

def calcOptimalPath(n, board):
    minCostMatrix = [[[float('inf'), None] for j in range(n)] for i in range(n - 1)]  # contains the cost of the optimal path to the top row along with the direction to move in for each position

    for i in reversed(range(1, n)):  # solve using a bottom-up DP starting from the top row
        for j in range(n):
            currentPos = (i - 1, j)

            left, up, right = float('inf'), float('inf'), float('inf')
            
            if j != 0:  # if we can move left
                left = sq2 * (board[currentPos[0]][currentPos[1]] + board[currentPos[0] + 1][currentPos[1] - 1]) / 2  # cost to move top left
            
            if j != n - 1:  # if we can move right
                right = sq2 * (board[currentPos[0]][currentPos[1]] + board[currentPos[0] + 1][currentPos[1] + 1]) / 2  # cost to move top right

            up = (board[currentPos[0]][currentPos[1]] + board[currentPos[0] + 1][currentPos[1]]) / 2  # cost to move straight up

            flag, minMoveCost = None, None  # flag takes values 0 (left), 1 (up), 2 (right)

            if i != n - 1:  # add remaining cost of path for each choice if not already on top row
                if j != 0:
                    left += minCostMatrix[i][j - 1][0]
                
                up += minCostMatrix[i][j][0]
                
                if j != n - 1:
                    right += minCostMatrix[i][j + 1][0]

            # get min cost and associated direction
            options = [left, up, right]
            minMoveCost = min(options)
            flag = options.index(minMoveCost)  # incase of same costs, direction priority: left > up > right

            minCostMatrix[i - 1][j] = [minMoveCost, flag]  # memoisation for next iteration

    optCost = float('inf')
    path = [[i, None] for i in range(n)]  # optimal path coordinates
    col = None
    dirFlag = None

    # get min total cost of path from bottom to top (i.e. optimal path cost), and starting column
    for i in range(n):
        # minCostMatrix[0][i][0] += (board[0][i] / 2)

        if minCostMatrix[0][i][0] < optCost:
            optCost = minCostMatrix[0][i][0]
            col = i

    # get path of optimal cost from bottom to top
    for i in range(n):
        dirFlag = minCostMatrix[0][col][1]  # get movement direction for optimal path
        path[i][1] = col  # update optimal path coordinates (initially all cols are set to None)
        
        if dirFlag == 0:
            col -= 1  # move left
        elif dirFlag == 2:
            col += 1  # move right

        # if flag == 1, stay in same col 

    print('Cost:', optCost)
    print('Path [row, column] from start to end:')
    for i in path:
        print(i)

def main():
    n, board = readFile()  # change board name if required on line 9

    if n > 1:
        calcOptimalPath(n, board)
    else:
        print('Already reached the top row')

main()