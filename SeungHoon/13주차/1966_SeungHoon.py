# [BOJ] 프린터 큐 / Silver 3 / 1h

T = int(input())

for i in range(T):
  N, M = map(int,input().split())
  arr = list(map(int,input().split()))

  ans = 1

  while arr:
    if(arr[0] < max(arr)):
      arr.append(arr.pop(0))
    else:
      if M == 0:
        break
      arr.pop(0)
      ans += 1
    if M > 0:
      M = M - 1
    else:
      M = len(arr) - 1
  
  print(ans)