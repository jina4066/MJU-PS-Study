import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = set(a)
d = dict()
index = 0

for v in sorted(s):
    d[v] = index
    index += 1

for v in a:
    print(d[v], end=' ')