from collections import deque

def solution(board):
    r, c = len(board), len(board[0])
    visited = [[False] * c for _ in range(r)]

    # 시작, 도착 좌표 찾기
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                start = (i, j)
            if board[i][j] == 'G':
                goal = (i, j)

    # BFS
    q = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]  # 상하좌우

    while q:
        x, y, cnt = q.popleft()
        if (x, y) == goal:
            return cnt

        for dx, dy in dirs:
            nx, ny = x, y
            # 벽이나 장애물 만날 때까지 이동
            while 0 <= nx + dx < r and 0 <= ny + dy < c and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy

            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))

    return -1
