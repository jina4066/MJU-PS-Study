# [BOJ] 잃어버린 괄호 / Silver 2 / 1h
str = input().split('-')

num = []

for i in str:
  sum = 0
  temp = i.split('+')
  for j in temp:
    sum += int(j)
  num.append(sum)

n = num[0]

for i in range(1, len(num)):
  n -= num[i]
print(n)

# 그리디 알고리즘으로 푸는 문제
# 괄호 없는 식이 주어졌을 때 - 이후에 +가 나오면 -뒤에 괄호를 쳤을 때 음수로 변해 값이 작아진다
# -를 기준으로 괄호를 쳐야한다
# -를 기준으로 split한 후 +를 기준으로 split하여 숫자만 남게 하고
# 숫자들을 더해서 결과를 리스트에 저장한다
# 이후 남은 값들을 빼서 결과를 출력