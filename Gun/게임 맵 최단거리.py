from collections import deque

def solution(maps):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]    
    q = deque([((0, 0), 1)])
    visited[0][0] = True
    
    while q:
        cur, depth = q.popleft()
        x, y = cur 
        if (x, y) == (n - 1, m - 1):
            return depth
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]    
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append(((nx, ny), depth + 1))
        
    return -1