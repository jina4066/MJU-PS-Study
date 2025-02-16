# [BOJ] 랜선 자르기 / Silver 2 / 30m
K, N = map(int,input().split())
arr = []
for i in range(K):
  temp = int(input())
  arr.append(temp)

start = 1
end = max(arr)

while start <= end:
  mid = (start + end) // 2
  count = 0
  
  for i in arr:
    count += i // mid
    
  if (count >= N):
    start = mid + 1
  else:
    end = mid - 1
    
print(end)

# 이전에 풀었던 2805/나무자르기 와 똑같은 문제
# 이분 탐색을 index가 아니라 길이를 기준으로 시행
# 랜선을 mid로 나눠(절반 자름) 카운트를 추가
# if문으로 랜선 자른수가 만들어야 될 랜선보다
# 큰 경우 랜선의 최소 길이를 중간 값보다 1 크게 설정
# 작은 경우 랜선의 최대 길이를 중간 값보다 1 작게 설정