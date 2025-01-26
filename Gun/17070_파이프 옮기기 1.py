import sys
input = sys.stdin.readline

n = int(input())
room = []
dp = [[0] * n for _ in range(n)]

for _ in range(n):
    room.append(list(map(int, input().split())))

if room[-1][-1] == 1:
    print(0)
    exit(0)

def find(loc):
    global dp
    s, e = loc
    r, c = e[0], e[1]
    dp[r][c] += 1
    
    if s[0] == e[0]: # 가로 방향
        if c + 1 < n:
            if room[r][c + 1] == 0:
                # 직진
                dest = (e, (r, c + 1))
                find(dest)
                # 대각선 탐색
                if r + 1 < n:
                    if room[r + 1][c + 1] == 0 and room[r + 1][c] == 0:
                        dest = (e, (r + 1, c + 1))
                        find(dest)
                
    elif s[1] == e[1]: # 세로 방향
        if r + 1 < n:
            if room[r + 1][c] == 0:
                dest = (e, (r + 1, c))
                find(dest)
                
                if c + 1 < n:
                    if room[r + 1][c + 1] == 0 and room[r][c + 1] == 0:
                        dest = (e, (r + 1, c + 1))
                        find(dest)

    else: # 대각선 방향
        if r + 1 < n:
            if room[r + 1][c] == 0:
                dest = (e, (r + 1, c))
                find(dest)
        if c + 1 < n:
            if room[r][c + 1] == 0:
                dest = (e, (r, c + 1))
                find(dest)
        if r + 1 < n and c + 1 < n:
            if room[r + 1][c + 1] == 0 and room[r][c + 1] == 0 and room[r + 1][c] == 0:
                dest = (e, (r + 1, c + 1))
                find(dest)

start, end = (0, 0), (0, 1)
find((start, end))
print(dp[-1][-1])