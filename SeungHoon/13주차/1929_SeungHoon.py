# [BOJ] 소수 구하기 / Silver 3 / 50m
M, N = map(int,input().split())
for i in range(M,N + 1):
  if(i == 1):
    continue
  for j in range(2, int(i ** 0.5) + 1):
    if i % j == 0:
      break
  else:
    print(i)

# M~N사이의 수들 중 소수를 찾기
# 각 수의 약수는 대칭되므로
# 제곱근을 구해 제곱근보다 작거나 같은 수까지만 비교
# 2 ~ 제곱근 사이 나누어 떨어진다면 break
# 아니면 해당 수를 출력