#[BOJ] 회의실 배정 / Gold 5 / 30m
import sys
N = int(sys.stdin.readline())

arr = []

for i in range(N):
  start, end = map(int,sys.stdin.readline().split())
  arr.append((start, end))

arr.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0
for i in range(N):
  if(arr[i][0] >= end):
    end = arr[i][1]
    count += 1
    
print(count)

# 처음 반복문 조건을 이런식으로 적었더니 틀렸다.
# count = 0
# start = 0
# end = 0
# for i in range(N):
#   if(arr[i][0] > end):
#     start = arr[i][0]
#     end = arr[i][1]
#     count += 1

# 생각 해보니 회의 시작시간은 굳이 필요가 없어서 빼고 반복문 조건을 수정하니 맞았다.
# 그리디 알고리즘으로 푸는 문제.
# 직전 회의가 끝나는 시간부터 시작하는 가장 빨리 끝나는 회의를 골라서
# 개수를 집계