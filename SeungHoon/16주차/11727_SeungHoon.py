# [BOJ] 2xn 타일링 / Silver 3 / 45m
n = int(input())
dp = [0] * 1001

dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
  dp[i] = dp[i - 1] + 2 * dp[i - 2]

print(dp[n]%10007)

# https://cijbest.tistory.com/21 블로그 참조
# n=3일때 부터 n=2, n=1의 모양이 있다
# n=1의 타일은 앞 모양만 다르고 두번씩 들어간다
# n=4일때도 n=3,n=2일때 모양이 있고, n=2가 두번씩 들어간다
# 점화식은 dp[i] = dp[i - 1] + 2 * dp[i - 2]과 같다