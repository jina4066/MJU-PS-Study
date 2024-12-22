N = int(input())

count = 0
ans = 666

while True:
  if ('666' in str(ans)):
    count = count + 1
  if count == N:
    break
  ans = ans + 1
  
print(ans)

# 수를 앞 뒤로 더해가면서 '666'이 들어가는 수 중 N번째로 작은 수를 찾는 문제
# 666에서 수를 하나씩 더 해가면서 '666'이 들어갈 때만 카운트를 증가
# 카운트가 입력받은 수와 같아지면 정답을 출력
