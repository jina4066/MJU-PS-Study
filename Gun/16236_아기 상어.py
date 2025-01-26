import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

board = []
bs = (0, 0)

for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            bs = (i, j)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

size, cnt, time = 2, 0, 0

def find_fish(loc):
    qq = deque([(0, loc)])
    dest = set()
    visited = [[False] * n for _ in range(n)]

    while qq:
        depth, l = qq.popleft()
        r, c = l
        visited[r][c] = True
 
        for i in range(4):
            x = dx[i] + r
            y = dy[i] + c

            if x < 0 or x >= n or y < 0 or y >= n:
                continue

            if not visited[x][y] and board[x][y] <= size:
                visited[x][y] = True # 이 부분 없으면 시간 초과
                qq.append((depth + 1, (x, y)))
                
                if 0 < board[x][y] < size:
                    dest.add((depth + 1, (x, y)))

    return sorted(list(dest), key=lambda x:[x[0], x[1][0], x[1][1]])

            
q = [(0, bs)]
board[bs[0]][bs[1]] = 0

while q:
    depth, loc = q[0]
    r, c = loc
    time += depth
    board[r][c] = 9

    if size <= cnt:
        size += 1
        cnt = 0
    cnt += 1

    q = find_fish(loc)
    board[r][c] = 0

print(time)