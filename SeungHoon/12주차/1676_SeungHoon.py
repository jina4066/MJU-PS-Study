# [BOJ] 팩토리얼 0의 개수 / Silver 5 / 40m

N = int(input())
count = 0

while(N > 1):
  count += N // 5
  N = N // 5

print(count)

# 팩토리얼로 얻을 수 있는 수를 인수분해 했을 때, 0이 늘어나는 순간은 10이 곱해지는 순간
# ==> 5의 개수를 찾는 문제
# 5의 배수는 5로 나눈 몫으로 계산