# [BOJ] 동전2 / Gold 5 / 1H
n,k = list(map(int,input().split()))

arr = []
for i in range(n):
  arr.append(int(input()))

dp = [10001] * (k+1)
dp[0] = 0

for i in arr:
  for j in range(i, k + 1):
    if(dp[j]>0):
      dp[j] = min(dp[j], dp[j-i] + 1)

if dp[k] == 10001:
  print(-1)
else:
  print(dp[k])

# DP를 입력받은 동전과 상관 없이 1~입력 최댓값 까지 구한다
# 현재 값에서 가져온 동전 값을 빼 주었을 때의 동전 사용 갯수에서
# 이전 코인들로만 조합했을 때 사용된 코인 개수를 비교해서 더 작은 값을dp 배열에 담는다