# [BOJ] 큐 / Silver 4 / 20m
import sys
N = int(sys.stdin.readline())

arr = []

for i in range(N):
  command = list(map(str,sys.stdin.readline().split()))
  
  if(command[0] == 'push'):
    arr.append(int(command[1]))
  elif(command[0] == 'pop'):
    if(len(arr) == 0):
      print(-1)
    else:
      num = arr[0]
      print(num)
      arr.remove(arr[0])
  elif(command[0] == 'size'):
    print(len(arr))
  elif(command[0] == 'empty'):
    if(len(arr) == 0):
      print(1)
    else:
      print(0)
  elif(command[0] == 'front'):
    if(len(arr) == 0):
      print(-1)
    else:
      print(arr[0])
  elif(command[0] == 'back'):
    if(len(arr) == 0):
      print(-1)
    else:
      index = len(arr)
      print(arr[index - 1])
      
# 간단한 큐 구현 문제. 이전에 풀었던 스택 구현과 크게 다를게 없다.
# 다만 시간제한이 빡세져서 sys을 썼다.
# 입력받은 문자열에 따라 큐의 동작을 구현한다.