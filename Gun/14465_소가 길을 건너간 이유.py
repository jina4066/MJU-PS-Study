import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())
a = [1] * n
broken = [int(input()) for _ in range(b)]

for i in range(b):
    a[broken[i] - 1] = 0


psum = sum(a[:k])
min_t = k - psum
last_idx = min(max(broken) + 1, n - k + 1)

for i in range(1, last_idx):
    psum = psum - a[i - 1] + a[i + k - 1]
    min_t = min(k - psum, min_t)
    
print(min_t)