# [BOJ] 행사장 대여 / Silver 5 / 40m
N = int(input())

arr = [[False for _ in range(500)]for _ in range(500)]

count = 0
min_x = 0
max_x = 500
min_y = 0
max_y = 0

for i in range(N):
  x1,y1,x2,y2 = map(int,input().split())
  min_x = min(min_x,x1)
  min_y = min(min_y,y1)
  max_x = max(max_x,x2)
  max_y = max(max_y,y2)

  for j in range(x1,x2):
    for k in range(y1,y2):
      arr[k][j] = True

for i in range(min_x,max_x):
  for j in range(min_y, max_y):
    if(arr[j][i] == True):
      count += 1

print(count)

# 입력받은 좌표와 이전에 입력받은 값을 
# 비교해 가장 큰 너비를 가지는 값을 이용
# 문제 조건에 따라 500*500의 False 배열을 만든 후
# 해당 좌표가 덮는 칸을 True로 표기
# 이후 True의 값을 전부 더함
