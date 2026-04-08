import sys
from collections import deque

def solution():
    (r, c) = list(map(int, sys.stdin.readline().split()))
    cheese = [ list(map(int, sys.stdin.readline().split())) for _ in range(r) ]
    map_size = r * c
    empty_num = 0
    time = 0 

    def melt_cheese() -> int: 
        queue = deque() 
        is_empty_area = [ [False for _ in range(c)] for _ in range(r)]
        is_visited = [ [False for _ in range(c)] for _ in range(r)]

        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue.append((0, 0))
        is_empty_area[0][0] = True
        result = 1
        melt_target = [] 

        while queue:
            cur = queue.popleft() 

            for d in dir: 
                nr = cur[0] + d[0] 
                nc = cur[1] + d[1] 

                if nr >= 0 and nr < r and nc >= 0 and nc < c and not is_empty_area[nr][nc]: 
                    
                    if cheese[nr][nc] == 0: 
                        queue.append((nr, nc))
                        is_empty_area[nr][nc] = True

        queue.append((0, 0))
        is_visited[0][0] = True

        while queue:
            cur = queue.popleft() 

            for d in dir: 
                nr = cur[0] + d[0] 
                nc = cur[1] + d[1] 

                if nr >= 0 and nr < r and nc >= 0 and nc < c and not is_visited[nr][nc]:

                    if cheese[nr][nc] == 0:
                        queue.append((nr, nc))
                        is_visited[nr][nc] = True
                        result += 1

                    if cheese[nr][nc] == 1:
                        empty_area_count = 0

                        for d in dir:
                            neighbor_r = nr + d[0]
                            neighbor_c = nc + d[1]

                            if cheese[neighbor_r][neighbor_c] == 0 and is_empty_area[neighbor_r][neighbor_c]:
                                empty_area_count += 1

                        if empty_area_count >= 2:
                            melt_target.append((nr, nc))
                            queue.append((nr, nc))
                            is_visited[nr][nc] = True
                            result += 1

        for m in melt_target: 
            cheese[m[0]][m[1]] = 0 

        return result 
         
    while empty_num < map_size: 
        empty_num = melt_cheese()
        time += 1 

    print(time)

solution()