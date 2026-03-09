import sys
import math
import heapq

def solution():
    input = [ int(x) for x in sys.stdin.readline().split() ]
    village_count = input[0]
    edge_count = input[1]
    party_location = input[2] 

    graph = [ [math.inf for _ in range(village_count + 1) ] for _ in range(village_count + 1) ]
    min_cost = [ [math.inf for _ in range(village_count + 1) ] for _ in range(village_count + 1) ]
    

    for _ in range(edge_count): 
        edge_info = [ int(x) for x in sys.stdin.readline().split() ]
        src = edge_info[0]
        dest = edge_info[1]
        weight = edge_info[2]

        graph[src][dest] = weight

    def dijkstra(start): 
        heap = []

        costs = [math.inf for _ in range(village_count + 1)]
        costs[start] = 0 
        heapq.heappush(heap, (0, start))

        while heap: 
            cur = heapq.heappop(heap) 
            cur_village = cur[1]
            cur_cost = cur[0]

            if cur_cost > costs[cur_village]: 
                continue

            for village, cost in enumerate(graph[cur_village]):
                if cost != math.inf and cost + cur_cost < costs[village]: 
                    costs[village] = cost + cur_cost
                    heapq.heappush(heap, (cost + cur_cost, village))

        for dest, cost in enumerate(costs):
            min_cost[start][dest] = cost

    for i in range(1, village_count + 1):
        dijkstra(i)
    
    result = 0

    for i in range(1, village_count + 1): 
        if i == party_location: continue
        result = max(result, min_cost[i][party_location] + min_cost[party_location][i])
    
    print(result)
solution() 