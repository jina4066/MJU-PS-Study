# [BOJ]최대공약수와 최소공배수 / Bronze 1 / 40m
x, y = map(int,input().split())

def gcd(x,y):
  while y != 0:
    temp = x % y
    x = y
    y = temp
  return x

print(gcd(x,y))
print(x*y//gcd(x,y))

# 유클리드 호제법을 이용하는 문제
# 처음엔 혼자 생각해서 풀려고 했다가
# 유클리드 호제법을 이용하니 순식간에 풀림