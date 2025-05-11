# [BOJ] 주몽 / Silver 4 / 45m
N = int(input())
M = int(input())
arr = list(map(int,input().split()))

arr.sort()
start = 0
end = len(arr) - 1
count = 0

while start < end:
  sum = arr[start] + arr[end]
  if(sum < M):
    start += 1
  elif(sum > M):
    end -= 1
  else:
    count += 1
    start += 1
    end -= 1
    
print(count)

# 아래처럼 풀면 역시나 시간 초과가 난다.
# count = 0
# for i in range(N):
#   target = arr[i]
#   for j in range(i + 1, N):
#     if(target + arr[j] == 9):
#       count += 1
# 투 포인터 알고리즘은 처음 들어봐서 하단 두 블로그를 참조했다.
# https://velog.io/@mjieun/Algorithm-%ED%88%AC-%ED%8F%AC%EC%9D%B8%ED%84%B0Two-Pointers-Python
# https://jminie.tistory.com/108 
