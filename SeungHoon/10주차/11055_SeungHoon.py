# [BOJ] 가장 큰 증가하는 부분 수열 / Silver 2 / 20m
N = int(input())

A = list(map(int,input().split()))

dp = [0] * N
dp[0] = A[0]

for i in range(N):
  for j in range(i):
    if(A[j] < A[i]):
      dp[i] = max(dp[i], dp[j] + A[i])
    else:
      dp[i] = max(dp[i], A[i])
      
print(max(dp))

# 11053번과 유사하다.
# 합을 구해야하기 때문에 0으로 dp 배열을 초기화
# 조건이 2개가 필요하다
# 1.증가하는 부분수열이면 dp[i] = max(dp[i], dp[j] + A[i])로 값을 갱신
# 그렇지 않다면 dp[i]와 dp[j]중 큰 값으로 갱신