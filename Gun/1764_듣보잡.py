import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = set()
b = set()
for _ in range(n):
    d.add(input().rstrip())

for _ in range(m):
    b.add(input().rstrip()) 

# 교집합 연산 - set 자료구조의 이용 (a.intersection(b) 도 가능)
db = sorted(d & b)

print(len(db))

for v in db:
    print(v)