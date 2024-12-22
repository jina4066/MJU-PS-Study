11053. 가장 긴 증가하는 부분 수열

# 부분 수열이란, 수열 중 순서를 그대로 유지하면서 그 안에서 나올 수 있는 수열의 부분집합이다.
# 단순히 이전 값의 정보를 통해서 수열의 길이를 구할 수 없으므로,
# 이중 반복문을 통한 DP를 통하여 해결하였다.
# 여기서 dp배열은 증가하는 수열의 길이를 저장한 배열이다.

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))
