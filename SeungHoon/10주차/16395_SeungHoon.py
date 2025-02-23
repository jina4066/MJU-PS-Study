# [BOJ] 파스칼의 삼각형 / Silver 5 / 30m
n, k = map(int,input().split())

up = 1
down = 1
count = 1

for i in range(n - 1, 0, -1):
  if(count == k):
    break
  up = up * i
  count += 1


for i in range(1, k):
  down = down * i

print(up // down)

# 문제에서 이항계수를 출력하라는 힌트를 준다
# 다만 C(n-1, k-1)이다
# 조합(Combination) 계산을 응용하여
# 분자는 n-1 ~ k까지 곱하고
# 분모는 1 ~ K까지 곱한 후
# 나눠준다.