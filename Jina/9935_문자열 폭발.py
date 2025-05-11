import sys

str = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []
bomb_len = len(bomb)

for i in range(len(str)):
    stack.append(str[i])
    if ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

if stack:
    print(''.join(stack))
else:
    print("FRULA")

# 첫번째 방법 시간초과

# import sys
# input = sys.stdin.readline

# str = input().rstrip()
# bomb = input().rstrip()

# while True:
#     if bomb in str:
#         str = str.replace(bomb,'')
#     else:
#         break

# if len(str) == 0:
#     print('FRULA')
# else:
#     print(str)


# 계속 시간초과 나는 두번째 방법..

# for char in str:
#     stack.append(char)
#     if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb:
#         del stack[-bomb_len]