N = int(input())
arr = list(map(int, input().split()))

odd = 0
even = 0
for i in range(N):
  if arr[i] % 2 == 1:
    odd += 1
  else:
    even += 1
    
if odd == even or odd == even + 1:
  print(1)
else:
  print(0)
  
# 길이가 N인 수열을 정리해서 홀수번째 원소는 모두 홀수, 짝수번째 원소는 모두 짝수인 수열이 성립 가능한지 판별하는 문제
# 먼저 배열안에 있는 홀수와 짝수의 개수를 카운트 한다.
# 홀수와 짝수갯수가 같거나, 홀수가 짝수보다 1개 더 많으면 문제가 없으므로 1을 출력
# 이 외에는 불가능하므로 0을 출력