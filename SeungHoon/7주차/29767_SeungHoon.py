# 점수를 최대로 / Silver 4 / 1h
import sys
N, K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

dp = [0] * N
dp[0] = arr[0]

for i in range(1,N):
  dp[i] = dp[i - 1] + arr[i]
dp.sort(reverse=True)
print(sum(dp[:K]))


# arr2 = arr[:]
# min_arr = []
# for i in range(N-K):
#   temp = min(arr2)
#   min_arr.append(temp)
#   arr2.remove(temp)

# sum = 0
# for i in range(len(arr)):
#   sum += arr[i] * K
#   if(arr[i] in min_arr):
#     continue
#   else:
#     K -= 1

# print(sum)
# 위 방식으로 풀면 시간 초과가 뜬다.
# 도저히 누적합을 어떻게 적용해야 할 지 모르겠어서 블로그를 참고했다.
# 주어진 교실의 점수의 구간합을 배열에 저장한 다음
# 내림차순으로 정렬해 K번째 index까지의 구간합을 구한다.
# https://cochin-man.tistory.com/59