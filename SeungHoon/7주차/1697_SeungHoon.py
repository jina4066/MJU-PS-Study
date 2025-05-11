# [BOJ] 숨바꼭질 / Silver 1 / 1h 30m
import sys
from collections import deque

def bfs(v):
  queue = deque()
  queue.append(v)
  while queue:
    V = queue.popleft()
    if(V == K):
      return visited[K]
    for i in (V + 1, V - 1, V * 2):
      if(0 <= i <= max and not visited[i]):
        visited[i] = visited[V] + 1
        queue.append(i)

N, K = map(int,sys.stdin.readline().split())
max = 100000
visited = [0] * (max + 1)
print(bfs(N))

# 너비 우선 탐색을 이용하는 문제
# 기존의 너비우선 탐색에서
# 노드가 v-1, v+1, V*2 3개로 펼처져 나갈 수 있다.
# 그리고 0보다 크고 제한값보다 작으며, 방문하지 않았으면 큐에 추가한다.
# 참고 : https://chancoding.tistory.com/193