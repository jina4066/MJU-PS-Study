import sys
# 파이썬의 기본 재귀 반복횟수 제한은 1000번인데,
# 이 문제는 50 * 50 = 2500 의 재귀 반복이 가능하므로 
# 재귀의 제한을 크게 설정함
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, visited):
    visited[y][x] = True

    for i in range(4):
        vx = x + dx[i]
        vy = y + dy[i]

        if vx < 0 or vy < 0 or vx >= m or vy >= n:
            continue
            
        if board[vy][vx] == 1 and not visited[vy][vx]:
            dfs(vx, vy, visited)


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    for y in range(n):
        for x in range(m):
            if board[y][x] == 1 and not visited[y][x]:
                count += 1
                dfs(x, y, visited)

    print(count)