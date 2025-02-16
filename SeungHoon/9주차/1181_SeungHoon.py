# [BOJ] 단어 정렬 / Silver 5 / 20m
N = int(input())

arr = []

for i in range(N):
  str = input()
  arr.append(str)
  
set_arr = set(arr)
arr = list(set_arr)
arr.sort()
arr.sort(key = len)

for i in range(len(arr)):
  print(arr[i])
  
# 파이썬 내장 함수를 잘 활용해야함
# set으로 중복을 없앰
# arr.sort()로 알파벳순으로 먼저 정렬
# arr.sort(key = len)으로 길이순으로 정렬