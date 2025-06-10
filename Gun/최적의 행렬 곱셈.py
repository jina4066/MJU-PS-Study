def solution(matrix_sizes):
    l = len(matrix_sizes)
    dp = [[0 for _ in range(l)] for _ in range(l)]
    
    for dist in range(1, l):
        for start in range(l - dist):
            a = start
            b = start + dist
            dp[a][b] = float('inf')
            for k in range(a, b):
                cost = matrix_sizes[a][0] * matrix_sizes[b][1] * matrix_sizes[k][1]
                dp[a][b] = min(dp[a][b], dp[a][k] + cost + dp[k + 1][b])
                
    return dp[0][-1]