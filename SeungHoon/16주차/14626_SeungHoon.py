# [BOJ] ISBN / Bronze 1 / 25m
str = input()
ans = 0
even = False

for i in range(13):
  if(str[i] == "*"):
    if (i % 2 != 0):
      even = True
    continue
  if(i % 2 == 0):
    ans += int(str[i])
  else:
    ans += int(str[i]) * 3
  
if even == True:
  for i in range(10):
    if(ans + (i * 3)) % 10 == 0:
      print(i)
      break
else:
  print(10 - ans % 10)

# 홀수 : 10의 배수인 몫으로 나눈 나머지에 대해 10에서 뺀 값이 *에 들어감
# 짝수 : (임의로 들어갈 값 *3 + 나머지 자릿수 규칙 합) / 10 == 0 인경우