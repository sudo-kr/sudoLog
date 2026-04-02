import sys
import math
from collections import deque

def solution():
    (col_size, row_size) = map(int, sys.stdin.readline().split())

    maze = [ list(map(int, sys.stdin.readline().strip())) for _ in range(row_size) ]
    move = [ [math.inf for _ in range(col_size)] for _ in range(row_size)]

    queue = deque() 
    queue.append((0, 0, 0))
    move[0][0] = 0
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while queue: 
        (cur_x, cur_y, break_count) = queue.popleft()

        if break_count > move[cur_y][cur_x]: 
            continue

        for d in directions: 
            nx = cur_x + d[0]
            ny = cur_y + d[1]
            nc = break_count

            if nx >= 0 and nx < col_size and ny >= 0 and ny < row_size: 
                if maze[ny][nx] == 1: 
                    nc += 1
                
                if nc < move[ny][nx]: 
                    queue.append((nx, ny, nc))
                    move[ny][nx] = nc

    print(move[row_size-1][col_size-1])

solution()