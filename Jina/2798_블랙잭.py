N, M = map(int,input().split())

nums = list(map(int,input().split()))
max = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = nums[i] + nums[j] + nums[k]
            if(sum <= M and sum > max):
                max = sum
print(max)

# 브루트포스 알고리즘을 사용하여 3장의 카드 조합을 모두 탐색한다.
