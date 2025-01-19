import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    a.append(int(input().rstrip()))

# 산술평균
print(round(sum(a) / n))

# 중앙값
print(sorted(a)[n // 2])

# 최빈값
d = dict(Counter(a))
max_cnt = max(d.values())
l = []

for v in d.keys():
    if d[v] == max_cnt:
        l.append(v)

if len(l) == 1:
    print(l[0])
else:
    print(sorted(l)[1])        
# 범위
print(max(a) - min(a))