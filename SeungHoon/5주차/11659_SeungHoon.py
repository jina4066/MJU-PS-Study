# 구간 합 구하기 4 / Silver 3 / 25m
N, M = map(int,input().split())

arr = list(map(int,input().split()))

prefix_sum = [0]
sum = 0
for i in range(len(arr)):
  sum += arr[i]
  prefix_sum.append(sum)

ans = []

for i in range(M):
  start, end = map(int,input().split())
  ans.append(prefix_sum[end] - prefix_sum[start-1])
  
for i in range(len(ans)):
  print(ans[i])
  
# ans = []

# for i in range(M):
#   start, end = map(int,input().split())
#   sum = 0
#   for i in range(start - 1,end):
#     sum += arr[i]
#   ans.append(sum)

# for i in range(len(ans)):  
#   print(ans[i])
  
# 주석 처리된, 평소에 풀던 방식으로 푸니 시간 초과가 뜬다.
# 누적합 방식으로 풀어야 한다.
# 부분합, 누적합 참고 자료 : https://velog.io/@qkrthdus605/Python-1%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%EB%B6%80%EB%B6%84%ED%95%A9%EA%B3%BC-%EB%88%84%EC%A0%81%ED%95%A9Prefix-Sum