import sys

def solution():
    meta_info = list(map(int, sys.stdin.readline().split()))
    product_count = meta_info[0]
    max_weight = meta_info[1] 

    product = [ list(map(int, sys.stdin.readline().split())) for _ in range(product_count)] 
    
    # dp[i][j]는 1~i번째 물건까지 사용해서 배낭의 무게가 최대 j까지 허용할 때 넣을 수 있을 최대 가치
    dp = [ [0 for _ in range(max_weight + 1)] for _ in range(product_count + 1)]

    for i in range(1, product_count + 1):
        weight = product[i-1][0]
        value = product[i-1][1]

        for j in range(1, max_weight + 1): 
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            if j-weight < 0: continue 

            dp[i][j] = max(dp[i][j], dp[i-1][j-weight] + value)

    print(dp[product_count][max_weight])

solution()
