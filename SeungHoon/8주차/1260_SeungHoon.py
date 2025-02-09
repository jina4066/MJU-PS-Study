# [BOJ] DFS와 BFS / Silver 2 / 1h
from collections import deque

N, M, V = map(int,input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for i in range(M):
  x, y = map(int,input().split())
  graph[x][y] = 1
  graph[y][x] = 1
  
visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)

def dfs(v):
  print(v, end=" ")
  visited1[v] = True
  for i in range(1, N + 1):
    if not visited1[i] and graph[v][i] == 1:
      dfs(i)
      
def bfs(v):
  queue = deque([v])
  visited2[v] = True
  while queue:
    v = queue.popleft()
    print(v, end = " ")
    for i in range(1, N + 1):
      if not visited2[i] and graph[v][i] == 1:
        queue.append(i)
        visited2[i] = True
        
dfs(V)
print()
bfs(V)

# 간단한 BFS와 DFS의 구현
# 아직까지 제대로 이해가 안된다.