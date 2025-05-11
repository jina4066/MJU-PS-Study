import sys
input = sys.stdin.readline

N, M = map(int, input().split())

a = set()
for i in range(N):
   a.add(input().rstrip())

b = set()
for i in range(M):
   b.add(input().rstrip())

lst = sorted(a.intersection(b))

print(len(lst))
for i in lst:
   print(i)