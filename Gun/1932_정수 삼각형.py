import sys
input = sys.stdin.readline

n = int(input())
t = []

for _ in range(n):
    t.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0: # 가장 왼쪽에 있는 수
            t[i][j] += t[i - 1][j]
        elif j == i: # 가장 오른쪽에 있는 수
            t[i][j] += t[i - 1][j - 1]
        else:
            t[i][j] += max(t[i - 1][j - 1], t[i - 1][j])

print(max(t[-1]))