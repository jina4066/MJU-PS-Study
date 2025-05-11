a, b, v = map(int, input().split())

day = (v - a) / (a - b) + 1

if day == int(day):
    print(int(day))
else:
    print(int(day)+1)

# import sys

# A, B, V = map(int, sys.stdin.readline().split())
# height = 0
# cnt = 0

# while True:
#     cnt += 1

#     height += A
#     if height >= V:
#         break

#     height -= B

# print(cnt)