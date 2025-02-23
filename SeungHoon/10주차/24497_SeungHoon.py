# [BOJ] blobnom / Silver 4 / 30
N = int(input())
arr = list(map(int,input().split()))
ans = max(arr)

for i in range(1, N - 1):
  if (min((arr[i - 1], arr[i + 1])) > 0):
    ans = max((ans, arr[i] + min((arr[i - 1], arr[i + 1]))))
    
print(ans)