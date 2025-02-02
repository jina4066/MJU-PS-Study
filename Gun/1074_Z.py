import sys

input = sys.stdin.readline
n, r, c = map(int, input().split())
ans = 0

while n > 0:
    n -= 1
    s = 2 ** n

    # 1사분면
    if c >= s and r < s:
        ans += s ** 2 * 1
        c -= s
    # 3사분면
    elif c < s and r >= s:
        ans += s ** 2 * 2
        r -= s
    # 4사분면
    elif c >= s and r >= s:
        ans += s ** 2 * 3        
        r -= s
        c -= s

print(ans)