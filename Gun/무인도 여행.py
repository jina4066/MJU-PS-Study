from collections import deque

def solution(maps):
    answer = []
    c, r = len(maps), len(maps[0])
    visited = [[False] * r for _ in range(c)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    for i in range(c):
        for j in range(r):
            if maps[i][j].isdigit() and not visited[i][j]:
                dates = int(maps[i][j])
                visited[i][j] = True
                q = deque([(i, j)])   
                while q:
                    x, y = q.popleft()       
                    for idx in range(4):
                        ni, nj = x + dx[idx], y + dy[idx]          
                        if ni < 0 or ni >= c or nj < 0 or nj >= r:
                            continue    
                        if maps[ni][nj].isdigit() and not visited[ni][nj]:
                            visited[ni][nj] = True
                            dates += int(maps[ni][nj])
                            q.append((ni, nj))         
                answer.append(dates)

    return sorted(answer) if answer else [-1]
