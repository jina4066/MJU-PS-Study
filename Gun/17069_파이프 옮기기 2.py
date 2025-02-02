import sys
input = sys.stdin.readline

n = int(input())
room = []
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

for _ in range(n):
    room.append(list(map(int, input().split())))

if room[-1][-1] == 1:
    print(0)
    exit(0)

dp[0][1][0] = 1 # 0,1 지점을 끝으로 하는 가로 방향의 파이프

for r in range(n):
    for c in range(2, n):
        if room[r][c]:
            continue
        dp[r][c][0] = dp[r][c - 1][0] + dp[r][c - 1][2]
        dp[r][c][1] = dp[r - 1][c][1] + dp[r - 1][c][2]

        if not room[r - 1][c] and not room[r][c - 1]:
            dp[r][c][2] = sum(dp[r - 1][c - 1])

print(sum(dp[-1][-1]))