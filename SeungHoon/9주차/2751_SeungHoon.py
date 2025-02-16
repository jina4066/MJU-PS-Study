# [BOJ] 수 정렬하기 2 / Silver 5 / 10m
import sys
N = int(input())

arr = []

for _ in range(N):
  arr.append(int(sys.stdin.readline()))
  
arr.sort()
for i in arr:
  print(i)
  
# 그냥 대충 입력 받으니 시간 초과가 떴다.
# sys.stdin.readline()으로 받아야 시간 초과가 안뜬다.