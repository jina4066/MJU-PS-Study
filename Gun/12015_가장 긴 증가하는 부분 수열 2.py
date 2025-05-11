import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [a[0]]

def bi(arr, num):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            end = mid - 1
        else:
            start = mid + 1

    return start

for num in a:
    if num > dp[-1]:
        dp.append(num)
    else:
        idx = bi(dp, num)
        dp[idx] = num

print(len(dp))

# Sol 2. bisect_left 사용
from bisect import bisect_left

for num in a:
    if num > dp[-1]:
        dp.append(num)
    else:
        idx = bisect_left(dp, num)
        dp[idx] = num

print(len(dp))
