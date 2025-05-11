N = int(input())

arr = [0] * 3001

for i in range(1, N+1):
  num = int(input())
  arr[i] = num
  
dp = [0] * 301
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
dp[3] = max(arr[1] + arr[3], arr[2] + arr[3])
  
for i in range(4, N+1):
  dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])
  
print(dp[N])

# 규칙 찾기
# 어디에서 올라왔는지(한칸전 or 두칸전)를 생각해야함
# max(직전칸에서 올라온 경우의 최댓값, 전전칸에서 올라온 경우의 최댓값)을 dp[n]에 할당
# 1h 걸림