import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

virus = 0
q = deque([virus])
visited = set([virus])

while q:
    com = q.popleft()

    for c in graph[com]:
        if c not in visited:
            visited.add(c)
            q.append(c)

print(len(visited) - 1)
