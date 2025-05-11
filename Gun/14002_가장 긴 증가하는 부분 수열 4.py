import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

res = []
x = max(dp)
print(x)

for i in range(n - 1, -1, -1):
    if x == dp[i]:
        res.append(a[i])
        x -= 1

print(*reversed(res))