# [BOJ] 파도반 수열 / Silver 3 / 45m
t = int(input())

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4,101):
  dp[i] = dp[i - 3]+ dp[i - 2]

for i in range(t):
  n = int(input())
  print(dp[n])

# DP문제
# 1~3번까지 삼각형 너비는 1이고 이후부터의 넓이는
# dp[i - 3]+ dp[i - 2] 다음 점화식을 따른다