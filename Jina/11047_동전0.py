import sys
input = sys.stdin.readline

# n: 동전 종류 수, k: 가치 합
n, k = map(int, input().split())
sum = 0

coinList = [int(input()) for _ in range(n)]
coinList.sort(reverse=True)

for i in coinList:
    sum += (k // i)
    k  = k % i

print(sum)