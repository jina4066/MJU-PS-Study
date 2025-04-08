# [BOJ] solved.ac / Silver 4 / 30m
import sys
def roundUp(num):
  if((num - int(num)) >= 0.5):
    return int(num) + 1
  else:
    return int(num)

n = int(sys.stdin.readline())

if n == 0:
  print(0)
else:
  arr = []

  for i in range(n):
    temp = int(sys.stdin.readline())
    arr.append(temp)

  arr.sort()
  ans = roundUp(n * 0.15)

  print(roundUp(sum(arr[ans:n-ans])/len(arr[ans:n-ans])))

# python에서 기본으로 제공하는 round함수를 이용하면
# .5에서 반올림 할 때 앞자리가 홀수면 올림, 짝수면 내림한다.
# 따라서 문제에 맞는 반올림 함수를 따로 만들어야 한다.
# n이 0이면 0을 출력하고
# n이 0ㅇ이 아니면 평균 경계를 구한다.
# 이후 정렬된 리스트를 경계를 기준으로 슬라이싱 하고, 나눈다