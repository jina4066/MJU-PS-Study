# [BOJ] 이항 계수 1 / Bronze 1 / 20m
N, K = map(int,input().split())

numerator = 1
denominator = 1

count = 0
for i in range(N,0,-1):
  if(count == K):
    break
  numerator = numerator * i
  count += 1
for i in range(K,0,-1):
  denominator = denominator * i
  
print(numerator // denominator)

# 이항계수 = 조합(Combination) 이었다.
# 분자, 분모를 입력값에서부터 역순으로 곱해준다
# 분자는 카운트를 추가해서 K번 반복하게 만든다.