# [BOJ] 연결 요소의 개수 / Silver 2 / 1h
import sys
sys.setrecursionlimit(10**6)
N, M = map(int,sys.stdin.readline().split())

def dfs(graph, v, visited):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
      
graph = [[] for _ in range(N + 1)]

for i in range(M):
  x, y = map(int,sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)
  
count = 0
visited = [False] * (N+1)
for i in range(1, N+1):
  if not visited[i]:
    dfs(graph, i, visited)
    count += 1
      
print(count)

# 간단한 그래프 탐색 문제
# 해당 문제는 DFS(깊이 우선 탐색)으로 풀었다.
# 먼저 그래프를 위한 2차원 배열을 만든 후
# graph[x].append(y)
# graph[y].append(x)
# 로 인접 리스트를 만든다.
# 방문 확인을 위한 visited 배열을 만든 후 False로 초기화 한다.
# dfs를 돌면서 그래프 배열, 인덱스, 방문 배열을 파라미터로 넘긴다.
# 그래프 안에 인접한 노드의 인덱스를 찾아가 방문 표시를 한다.
# 하나의 싸이클을 찾고 난 후 count + 1을 해준다.
# 시간초과가 떠서 sys.stdin.readline()을 이용했다.