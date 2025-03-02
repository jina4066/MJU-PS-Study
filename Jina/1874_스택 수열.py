import sys

n = int(sys.stdin.readline().strip())

result = []
stack = []

# 1~n 중에서 현재 가리키고 있는 값
cur = 1

for _ in range(n):
  seq = int(sys.stdin.readline().strip())
  
  # seq <= cur 만족할 때까지 반복
  # 즉, seq까지 스택에 저장
  while cur <= seq:
    stack.append(cur)
    result.append('+')
    cur += 1

  # while문을 실행한 seq값이 stack에 마지막에 삽입된 값과 같으면 실행
  if stack[-1] == seq:
    stack.pop()
    result.append('-')
  # 불가능하면 NO 출력
  else:
    result.clear()			
    result.append('NO')	
    break					

for answer in result:
  print(answer)