# 스택 / Silve 4 / 20m

N = int(input())

arr = []
ans = []

for i in range(N):
  command = list(map(str, input().split()))
  
  if(command[0] == 'push'):
    arr.append(int(command[1]))
  elif(command[0] == 'top'):
    if(len(arr) != 0):
      target = len(arr)
      ans.append(arr[target - 1])
    else:
      ans.append(-1)
  elif(command[0] == 'size'):
    ans.append(len(arr))
  elif(command[0] == 'empty'):
    if(len(arr) == 0):
      ans.append(1)
    else:
      ans.append(0)
  elif(command[0] == 'pop'):
    if(len(arr) == 0):
      ans.append(-1)
    else:
      target = len(arr)
      pop_int = arr[target - 1]
      ans.append(pop_int)
      arr.pop()
      
for i in range(len(ans)):
  print(ans[i])
  
# 간단한 스택 구현 문제
# 입력값 분리가 또 헷갈렸다. 잘 기억하자.
# 그리고 top에서 인덱스 생각을 안해서 한번 틀렸었다.
# 로직 구현에 어려움은 없었음