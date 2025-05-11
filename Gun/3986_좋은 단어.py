import sys

input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    word = list(input().rstrip())
    last = word[0]
    stack = [last]

    for c in word[1:]:
        if stack:
            if c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)

    if len(stack) == 0:
        cnt += 1

print(cnt)