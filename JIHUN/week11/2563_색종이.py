# 100x100 크기의 도화지를 0으로 초기화
grid = []
for _ in range(100):
    row = [0] * 100  # 한 줄(100칸)을 0으로 초기화
    grid.append(row)

paper = int(input())  # 색종이 개수 입력

# 색종이 붙이기
for _ in range(paper):
    x, y = map(int, input().split())  # 색종이 위치
    for i in range(x, x + 10):  # 가로 10칸
        for j in range(y, y + 10):  # 세로 10칸
            grid[i][j] = 1  # 색종이가 붙은 부분을 1로 변경

# 검은색 영역 계산
area = 0
for row in grid:
    area += sum(row)  # 각 행의 1의 개수를 더함

print(area)  # 출력

# 총 색종이 넓이에서 겹치는 부분을 제거하는 방식을 쓰다가 실패하여 gpt의 방식을 참고했다.
# 수학적인 방법보다 효율적으로 생각하는 방식으로 생각하는 능력을 길러야 할 것 같다,,