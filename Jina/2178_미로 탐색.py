from collections import deque
import sys

# BFS
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            # 미로의 범위 안인지 확인
            if 0 <= next_x < N and 0 <= next_y < M: 
                
                if graph[next_x][next_y] == 1:
                    queue.append((next_x, next_y))
                    graph[next_x][next_y] = graph[x][y] + 1
    return graph[N - 1][M - 1]

input = sys.stdin.readline
N, M = map(int, input().split())

# 2차원 리스트 생성
graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]

queue = deque([(0, 0)])

# 이동 표현 (위, 아래, 오른쪽, 왼쪽)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0

print(bfs())

