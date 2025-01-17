# N = int(input())

# arr = []

# for i in range(N):
#   arr.append(i+1)

# index = 0
# while len(arr)>1:
#   arr.remove(arr[0])
#   arr.append(arr[0])
#   arr.remove(arr[0])

# print(*arr)

# 카드2 / Silver 2 / 15m
from collections import deque

N = int(input())

arr = deque(range(1, N+1))

while len(arr) > 1:
  arr.popleft()
  arr.append((arr.popleft()))
  
print(arr[0])

# 위에 주석 처리된 방식대로 풀어도 작동은 정상적으로 한다
# 다만 시간 초과가 뜨기 때문에 파이썬에서 제공하는 deque를 쓰기를 권유 받았다.
# deque를 쓸 뿐 로직은 똑같다.

# https://velog.io/@error_io/%EB%B0%B1%EC%A4%80-2164-%EC%B9%B4%EB%93%9C2-Python
# 추가로 여기에 수학적으로 푼 방법도 있다.