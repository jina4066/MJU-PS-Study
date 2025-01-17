# 괄호 / Silver 4 / 10m
N = int(input())

ans = []

for i in range(N):
  str = input()
  arr = []
  for j in str:
    if(j == '('):
      arr.append(j)
    if(len(arr) != 0 and j == ')'):
      arr.pop()
    elif(len(arr) == 0 and j == ')'):
      arr.append(j)
      break
  if(len(arr) == 0):
    ans.append('YES')
  else:
    ans.append('NO')
    
for i in range(len(ans)):
  print(ans[i])
  
# 출력형식을 항상 잘 생각하자. 매번 다 맞혀놓고 출력 형식 때문에 틀린다!
# 간단한 스택 구현문제. 조건을 3개로 나눴다
# 1. ( 가 들어오면 무조건 스택에 추가
# 2. )가 들어왔을 때 스택이 비어있지 않다면 pop
# 2-1. )가 들어왔을 때 스택이 비어있으면 )를 스택에 넣고 break
# 결과적으로 배열의 길이가 0 이면 괄호가 완성
# 길이가 0이 아니면 괄호가 valid하지 않다.