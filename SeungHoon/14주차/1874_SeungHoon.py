# [BOJ] 스택 수열 / Silver 2 / 40m
n = int(input())

count = 1
temp = True
stack = []
op = []

for i in range(n):
  num = int(input())
  while count <= num:
    stack.append(count)
    op.append('+')
    count += 1
  
  if stack[-1] == num:
    stack.pop()
    op.append('-')
  
  else:
    temp = False
    break

if temp == False:
  print('NO')
else:
  for i in op:
    print(i)

# stack을 구현하는 문제
# 수를 입력 받은 후
# 해당 수 이하의 숫자까지 스택에 넣은후
# op배열에 +를 추가한다.
# 이후 입력값과 스택 맨 위의 숫자가 동일하면 제거하고,
# op 배열에 -를 추가한다.
# 일치하지 않으면 스택 수열을 만들 수 없으므로 temp를 False로 둔다
# 이후 temp값이 false면 NO를, True면 op 배열을 출력한다.