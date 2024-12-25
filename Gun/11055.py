11055. 가장 큰 증가하는 부분 수열

# 이 문제 역시 가장 긴 증가하는 부분 수열 문제와 비슷하게 DP로 풀 수 있다.
# 다른 점은 증가하는 수열의 합을 저장한다(배열 s)는 점에서 다르다.

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = a[:]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            s[i] = max(s[i], s[j] + a[i])
            
print(max(s))
