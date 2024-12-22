2156. 포도주 시식

# n: 1 ~ 1000
# 나열된 포도주 중 최대로 마실 수 있는 포도주의 양을 구하기
# 단 연속 세 잔은 마실 수 없음
# 마신 포도주의 양을 기억하고 이를 활용하여 최대 양을 구하면 되므로,DP를 사용하는 것이 적절함

# i번째 잔을 마실 때, i - 1번째 잔을 마셨는지, i - 2번째 잔을 마셨는지를 저장하여 활용
# 또한 빈 잔이 올 수 있으므로 i - 3번째 잔까지 고려 (이 부분에서 잠시 헤맸음)

import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

dp = [[0] * n for _ in range(2)]

# 두 잔까지는 연속으로 마셔도 상관없으므로 조건문을 이용하여 처리함
if n <= 2:
    print(sum(a))

else:
    dp[0][0] = a[0]
    dp[0][1] = a[1]
    dp[1][1] = a[0] + a[1]
    dp[0][2] = max(dp[0][0], dp[1][0]) + a[2]
    dp[1][2] = dp[0][1] + a[2]
    
    for i in range(3, n):
        dp[0][i] = max(dp[0][i - 2], dp[1][i - 2], dp[0][i - 3], dp[1][i - 3]) + a[i]
        dp[1][i] = dp[0][i - 1] + a[i]

    print(max(dp[0][-2], dp[0][-1], dp[1][-2], dp[1][-1]))


