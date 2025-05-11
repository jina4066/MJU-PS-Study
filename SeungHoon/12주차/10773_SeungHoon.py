# [BOJ] 제로 / Silver 4 / 15m
K = int(input())
ans = []
for i in range(K):
  num = int(input())
  if(num != 0):
    ans.append(num)
  elif(num == 0):
    ans.pop()

print(sum(ans))

# 이게 왜 실버4일까
# 입력값이 0이 아니면 배열에 숫자를 추가
# 입력값이 0이면 배열 끝 숫자를 pop
# 배열 안의 숫자들의 합을 출력