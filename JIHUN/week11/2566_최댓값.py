grid = []

for _ in range(9):
    row = list(map(int, input().split()))
    grid.append(row)

maxnum = grid[0][0]
maxrow = 0
maxcol = 0

for i in range(9):
    for j in range(9):
        if grid[i][j] > maxnum:
            maxnum = grid[i][j]
            maxrow = i
            maxcol = j
print(maxnum)
print(maxrow+1, maxcol+1)

#2차원 배열을 생성하는 것부터 생각하기 어려웠다. 순회하며 출력값을 업데이트 하는 방법을 생각했고 실행했다.
