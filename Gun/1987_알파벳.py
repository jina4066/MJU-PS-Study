import sys
input = sys.stdin.readline
# pypy로 채점하여 재귀 제한을 설정하지 않음

r, c = map(int, input().split())
board = [[] for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]
max_depth = 0

for i in range(r):
    alphbets = input().rstrip()
    for a in alphbets:
        board[i].append(ord(a) - 65)
    
visited = set([board[0][0]])

# 재귀 정지 조건: 더 이상 탐색할 곳이 없을 때 리턴

def dfs(start, depth):
    global max_depth
    if depth == 26:
        print(depth)
        exit()
        
    max_depth = max(max_depth, depth)
    
    for i in range(4):
        sx, sy = start
        x, y = sx + dx[i], sy + dy[i]
        
        if x < 0 or x >= r or y < 0 or y >= c:
            continue

        cur = board[x][y]
        
        if cur not in visited:
            visited.add(cur)
            dfs((x, y), depth + 1)
            visited.remove(cur)
            
    return

dfs((0, 0), 1)
print(max_depth)