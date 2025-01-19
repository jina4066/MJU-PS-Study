import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

def l(arr):
    n = len(arr)
    dp = [arr[0]]
    seq = [1]
    max_seq = 1
    
    for i in range(1, n):
        if dp[-1] < arr[i]:
            dp.append(arr[i])
            seq.append(max_seq + 1)
        else:
            idx = bisect_left(dp, a[i])
            dp[idx] = arr[i]
            seq.append(idx + 1)
            
        max_seq = max(max_seq, seq[-1])  
    
    return seq

s = l(a)
x = max(s)
print(x)

res = []
for j in range(N - 1, -1, -1):
    if s[j] == x:
        res.append(a[j])
        x -= 1

print(*res[::-1])