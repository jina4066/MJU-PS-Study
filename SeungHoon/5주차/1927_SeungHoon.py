# 최소 힙 / Silver 2 / 30m
import heapq
import sys
N = int(sys.stdin.readline())

heap = []

for i in range(N):
  num = int(sys.stdin.readline())
  if(num == 0):
    if(len(heap) == 0):
      print(0)
    else:
      print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, num)

# 아래처럼 list로 구현하고, 매번 sort()를 쓰면 시간초과가 뜬다
# arr = []

# for i in range(N):
#   num = int(input())
#   if(num == 0):
#     if(len(arr) == 0):
#       print(0)
#     else:
#       print(arr[0])
#       arr.remove(arr[0])
#   else:
#     arr.append(num)
#   arr.sort()

# 파이썬 자료형중 heapq를 이용했다. 기본이 최소힙으로 구현돼있음
# 추가로 input()때문에 시간 초과가 떠서 sys를 이용했다.