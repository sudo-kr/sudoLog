import sys
import math

def solution():
    red = 0 
    green = 1  
    blue = 2

    n = int(sys.stdin.readline())
    costs = [ [int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    dp = [ [math.inf for _ in range(n)] for _ in range(n)]
    candidates = [[1, 2], [0, 2], [0, 1]]

    for i in range(3):
        dp[0][i] = costs[0][i]

    for i in range(1, n):
        for j in range(3):
            cost = costs[i][j]
            for k in candidates[j]:
                dp[i][j] = min(dp[i-1][k] + cost, dp[i][j])

    print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))

solution() 