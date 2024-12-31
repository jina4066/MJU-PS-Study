# n = int(input())  #수의 개수 입력 받기
# nums = []

# for _ in range(n):
#     nums.append(int(input()))

# nums.sort()

# for num in nums:
#     print(num)


import sys

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for num in nums:
    print(num)

