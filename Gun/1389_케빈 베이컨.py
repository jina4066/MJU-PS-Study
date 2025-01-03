1. BFS 풀이

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

min_kb = n ** 2
answer = 0

for i in range(n):
    q = deque([(i, 0)])
    kb = 0
    visited = set()
    visited.add(i)
    
    while q:
        x, dist = q.popleft()
        kb += dist

        for y in graph[x]:
            if y not in visited:
                visited.add(y)
                q.append((y, dist + 1))

    if min_kb > kb:
        min_kb = kb
        answer = i + 1

print(answer)


2. Floyd-warshall 풀이

import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0
            break

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

rank = []
for i in range(1, n + 1):
    rank.append([i, sum(graph[i][1:])])

print(sorted(rank, key=lambda x: x[1])[0][0])