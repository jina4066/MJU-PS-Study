import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a, b = [], []
max_violation = 0

for _ in range(n):
    idx, deadline = map(int, input().split())
    arr = [deadline] * idx
    a.extend(arr)
    
for _ in range(m):
    idx, speed = map(int, input().split())
    arr = [speed] * idx
    b.extend(arr)

for i in range(100):
    if a[i] < b[i]:
        violation = b[i] - a[i]
        max_violation = max(violation, max_violation)

print(max_violation)