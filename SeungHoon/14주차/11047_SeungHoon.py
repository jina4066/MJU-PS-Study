# [BOJ] 동전 0 / Silver 4 / 30m
N, K = map(int,input().split())

sum = 0
count = 0
arr = []

for i in range(N):
  temp = int(input())
  arr.append(temp)

arr.sort(reverse=True)

for i in arr:
  count += K // i
  K = K % i

print(count)

# 그리디를 이용하는 문제
# 입력값을 배열에 저장 후 (오름차순으로 들어옴)
# 내림차순으로 정렬한다.
# 가장 큰 화폐 단위부터 거슬러
# count에 K를 화폐단위로 나눈 몫을 저장하고
# K를 나눈 나머지 값으로 갱신하며 반복한다.