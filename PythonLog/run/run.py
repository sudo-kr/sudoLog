import sys
import math
from collections import deque

def solution():
    building_count = int(sys.stdin.readline())
    time = [0]
    end_time = [0 for _ in range(building_count + 1)] 
    indegree = dict() 
    outdegree = dict()

    for num in range(1, building_count + 1):
        indegree[num] = 0
        outdegree[num] = []

    for num in range(1, building_count + 1):
        infos = list(map(int, sys.stdin.readline().split()))

        for i, info in enumerate(infos): 
            if i == 0: 
                time.append(info)
            elif info != -1: 
                indegree[num] += 1 
                outdegree[info].append(num)

    queue = deque()

    for num in range(1, building_count + 1): 
        if indegree[num] == 0:
            queue.append(num)
            end_time[num] = time[num] 

    while queue: 
        cur = queue.popleft()

        for out in outdegree[cur]:
            indegree[out] -= 1
            end_time[out] = max(end_time[cur] + time[out], end_time[out])

            if indegree[out] == 0:
                queue.append(out)

    end_time = end_time[1:]
    print("\n".join(map(str, end_time)))

solution()