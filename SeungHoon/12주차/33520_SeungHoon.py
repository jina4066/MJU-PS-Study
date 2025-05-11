# [BOJ] 초코바 만들기 / Silver 5 / 20m
import sys

N = int(sys.stdin.readline().strip())

max_width = 0
max_height = 0

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    max_width = max(max_width, min(a, b))
    max_height = max(max_height, max(a, b))

print(max_width * max_height)

# N = int(input())

# width = set()
# height = set()

# for i in range(N):
#   a, b = map(int,input().split())
#   width.add(min(a,b))
#   height.add(max(a,b))

# print(max(width) * max(height))

# 위와 같이 풀면 시간초과가 뜬다
# 어차피 최소값중 최대, 최대값들 중 최대만 필요하니
# 굳이 배열을 생성하지 않고 값을 갱신해준다.

# 회전도 고려해야 하므로 입력받은 좌우 길이중 작은건 width, 큰건 height로 고정한다.
# width중 최대와 height중 최대를 곱한 값을 출력한다.