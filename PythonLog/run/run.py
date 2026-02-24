from collections import deque
import sys

def solution(): 
    size = sys.stdin.readline().split()

    n = int(size[0])
    m = int(size[1])
    maze = [[0 if char == '1' else -1 for char in sys.stdin.readline().strip()] for _ in range(n)]
    is_visited = [[False for _ in range(m)] for _ in range(n)]
    result = 0 
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def extract(): 
        queue = deque()
        queue.append((0, 0))
        is_visited[0][0] = True

        while queue: 
            current = queue.popleft()

            for i in range(4):
                nx = current[0] + dir[i][0]
                ny = current[1] + dir[i][1]
                if nx >= 0 and ny >= 0 and nx < n and ny < m and not is_visited[nx][ny] and maze[nx][ny] == 0: 
                    is_visited[nx][ny] = True
                    queue.append((nx, ny))
                    maze[nx][ny] = maze[current[0]][current[1]] + 1

    extract()
    print(maze[n-1][m-1] + 1)


solution()