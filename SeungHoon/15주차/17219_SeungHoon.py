# [BOJ] 비밀번호 찾기 / Silver 4 / 15m
import sys

N,M = map(int,sys.stdin.readline().split())

arr = dict()

for i in range(N):
  admin, password = map(str, sys.stdin.readline().split())
  arr[admin] = password

for i in range(M):
  temp = input()
  if temp in arr:
    print(arr[temp])

# Dictionary를 이용하는 간단한 문제
# 사이트 주소와 비밀번호를 입력받은 후
# dict에 key, value로 저장
# 이후 반복문을 돌면서 
# if temp in arr: 를 이용해
# 찾고자하는 사이트의 비밀번호를 출력