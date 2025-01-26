# 나무 자르기 / Silver 2 / 45m
import sys
N, M = map(int,sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(arr)

while start <= end:
  sum = 0
  mid = (start + end) // 2
  
  for i in arr:
    if(i > mid):
      sum += i - mid
  if(sum < M):
    end = mid - 1
  else:
    start = mid + 1
  
print(end)

# 이진 탐색으로 푸는 문제
# 기본적인 이진 탐색과 같지만 인덱스를 찾는 문제가 아니라서 헷갈렸음
# 34%에서 시간초과가 떠서 pypy3로 돌렸다.