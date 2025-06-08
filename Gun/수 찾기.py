import sys
input = sys.stdin.readline

n = int(input())
nums = set(list(map(int, input().split())))
m = int(input())
inputs = list(map(int, input().split()))

for num in inputs:
    print(len(nums & {num}))