# [BOJ] 최대 힙 / Silver 2 / 20m
import heapq
import sys

N = int(sys.stdin.readline().strip())

max_heap = []

for _ in range(N):
    temp = int(sys.stdin.readline().strip())
    if temp == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(max_heap))
    else:
        heapq.heappush(max_heap, -temp)

# N = int(sys.stdin.readline())

# arr = []

# for i in range(N):
#   temp = int(sys.stdin.readline())
#   if(temp == 0):
#     if(len(arr) == 0):
#       print('0')
#     else:
#       max_num = max(arr)
#       print(max_num)
#       arr.remove(max_num)
#   else:
#     arr.append(temp)

# 위 방법대로 풀면 시간 초과가 뜬다
# 0이 입력되면 print(-heapq.heappop(max_heap))로 최댓값을 출력 후 제거한다.
# 0이 아닌 경우 최대 힙 구현을 위해 음수로 삽입한다.