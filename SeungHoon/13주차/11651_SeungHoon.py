# [BOJ] 좌표 정렬하기 2 / Silver 5 / 20m
N = int(input())

arr = []

for i in range(N):
  x, y = map(int,input())
  arr.append((x,y))

arr.sort(key = lambda x : (x[1], x[0]))

for i in arr:
	print(i[0], i[1])
     
# 좌표를 오름차순으로 정렬하는 문제
# x, y값을 입력 받은 후
# sort 메소드의 lambd를 이용해서
# y값을 우선으로 정렬하고
# y값이 같으면 x값으로 정렬한다.