import sys

input = sys.stdin.readline

n, k = map(int, input().split())
bag = [0] + []
dp = [[0] * (k + 1) for _ in range(n + 1)]

for _ in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= bag[i][0]:
            dp[i][j] = max(dp[i - 1][j], bag[i][1] + dp[i - 1][j - bag[i][0]])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])