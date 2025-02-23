# [BOJ] 가장 긴 부분수열 / Silver 2 / 40m

N = int(input())

arr = list(map(int,input().split()))
dp = [1] * N

for i in range(1, N):
  for j in range(i):
    if(arr[j] < arr[i]):
      dp[i] = max(dp[i], dp[j] + 1)
      
print(max(dp))

# dp배열을 1로 초기화(연속되지 않는 수열의 길이는 1이기 때문)
# 첫번째 반복문이 뒤의 수
# 두번째 반복문이 그 이전의 수들
# 이전의 수(j)가 이후의 수(i)보다 작으면 현재 dp[i]의 값과 dp[j]+1을 비교해 큰 값을 dp에 배치
# 이후 dp 배열의 최댓값 출력

# https://it-adventures.tistory.com/109