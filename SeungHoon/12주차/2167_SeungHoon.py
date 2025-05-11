# [BOJ] 2차원 배열의 합 / Silver 5 / 50m
N, M = map(int,input().split())
arr = []

for i in range(N):
  temp = list(map(int,input().split()))
  arr.append(temp)

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
  for j in range(1, M + 1):
    dp[i][j] = arr[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

K = int(input())

for i in range(K):
  i, j, x, y = map(int,input().split())
  print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])

# 누적합 문제이고, 점화식을 세우는 문제
# x,y까지의 합을 구하고 싶으면
# x, y-1까지의 합 + x-1,y까지의 합을 구하고
# 중복된 x-1,y-1까지의 합을 빼주면 된다.
# 출력 또한 마찬가지로
# 처음부터 출력 해야햐는 인덱스 까지의 합에서
# 겹치지 않는 부분을 빼고, 중복되게 빠진 부분을 더해줘야 한다.
# 그림과 함께 적힌 설명은 아래를 참고
# https://velog.io/@seungjae/%EB%B0%B1%EC%A4%80-2167%EB%B2%88-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%ED%95%A9-Python-DP