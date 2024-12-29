n, m = map(int, input().split())
a = list(map(int, input().split()))

s = 0
left = 0
ans = []

for right in range(n):
    s += a[right]
    
    while s >= m:
        ans.append(right - left + 1)
        s -= a[left]
        left += 1

if ans:
    print(sorted(ans)[0])
else:
    print(0)