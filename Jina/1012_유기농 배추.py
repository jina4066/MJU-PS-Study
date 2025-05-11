import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정

def dfs(x, y):
  if x <= -1 or x >= N or y<= -1 or y>= M:
    return False

  if graph[x][y] == 1:
    graph[x][y] = 0

    for i in range(4):
      dfs(x + dx[i], y+dy[i])

    return True
  return False


T = int(sys.stdin.readline()) 

dx = [-1, 1, 0, 0] # 상하좌우 이동
dy = [0, 0, -1, 1]

answer = []

for _ in range(T):
  M, N, K = list(map(int, sys.stdin.readline().split()))  

  graph = [[0]*M for _ in range(N)]

  for _ in range(K):
    x, y = map(int, input().split())
    graph[y][x] = 1

  cnt = 0
  for i in range(N):
    for j in range(M):
      if dfs(i, j):
        cnt +=1

  print(cnt)