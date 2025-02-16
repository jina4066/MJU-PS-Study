# [BOJ] AC / GOLD 5 / 1h
import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    check, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            check += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if check % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if check % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
            
  # count =0
  # for i in P:
  #   if(i == 'R'):
  #     count += 1
      
  # if(count % 2 != 0):
  #   arr = arr[::-1]
  
  # for i in P:
  #   if(i == 'D'):
  #     if(len(arr) != 0):
  #       arr.pop(0)
  #     else:
  #       print('error')
  #       break
  
  # if(len(arr) != 0):
  #   print("[" + ",".join(map(str, arr)) + "]")
  # 이렇게 풀면 시간 초과가 뜬다
  # 큐를 사용해서 푸는 문제
  # 뒤집는 연산 'R'을 R이 입력 될 때 마다 수행하는게 아니라
  # 홀수번 입력 되었을 때 한번만 실행하면 된다.