# [BOJ] 숫자 카드 / Silver 5 / 20m
N = int(input())
card = list(map(int,input().split()))
  
M = int(input())
det = list(map(int,input().split()))

dic = {}

for i in card:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1
    
for i in det:
  if i in dic:
    print(dic[i], end=" ")
  else:
    print(0, end=" ")

# 예전에 풀었던 10816(숫자 카드2) 코드와 거의 일치한다.
# dictionary 자료구조를 이용해 입력받은 카드의 위치에 1을 넣는다
# 이후 검사할 배열을 돌면서 dictionary에 해당하는 인덱스의 값이 있으면 1을, 아니면 0을 찍는다.