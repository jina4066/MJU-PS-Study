import sys

def dfs(idx) : 
    global visited
    visited[idx] = 1
    print(idx, end=' ')
    for next in range(1, N + 1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end = ' ')
        for next in range(1, N + 1):
            if not visited[next] and graph[cur][next]:
                visited[next] = 1
                q.append(next)
                

input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

# 그래프 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# dfs
dfs(V)
print()

# bfs
visited = [0] * (N + 1)
q = [V]
visited[V] = 1
bfs()