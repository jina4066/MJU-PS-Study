T = int(input())

ans = []
dp = [0] * 1000001
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(T):
  num = int(input())
  for j in range(3,num):
    dp[j] = dp[j-3] + dp[j-2] + dp[j-1]
  ans.append(dp[num-1])
  
for i in range(len(ans)):
  print(ans[i])
  
# 규칙 찾는데 한참 걸렸다
# 4번째 경우의 수 = 첫번째 + 두번째 + 세번째 경우의 수인것을 활용해
# i번째는 i-3 + i-2 + i-1의 경우의 수 인것을 알아낸다.
# 출력 형식을 잘 맞추자. 다 풀어놓고 출력 형식 때문에 틀렸다.
# 45분 걸림