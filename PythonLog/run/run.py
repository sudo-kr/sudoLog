import sys 
from collections import deque

def solution():
    size_input = sys.stdin.readline().split()
    row_size = int(size_input[1])
    col_size = int(size_input[0])
    warehouse = [ [ int(x) for x in sys.stdin.readline().split() ] for _ in range(row_size) ]
    
    def time_goes() -> int: 
        queue = deque() 
        result = 0 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(0, row_size):
            for j in range(0, col_size):
                if warehouse[i][j] == 1: 
                    queue.append((i, j, 1))

        
        while queue:
            cur = queue.popleft()

            for i in range(0, 4):
                nr = cur[0] + directions[i][0]
                nc = cur[1] + directions[i][1]

                if nr >= 0 and nr < row_size and nc >= 0 and nc < col_size and warehouse[nr][nc] == 0:
                    warehouse[nr][nc] = cur[2] + 1 
                    queue.append((nr, nc, cur[2] + 1))


        for i in range(0, row_size):
            for j in range(0, col_size):
                if warehouse[i][j] == 0:
                    return -1
                else: 
                    result = max(result, warehouse[i][j] - 1)

        return result

    print(time_goes())



solution()