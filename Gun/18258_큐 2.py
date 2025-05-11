import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    
    stack = deque()
    count = int(input())
    for _ in range(count):
        command = (list(map(str, input().split())))
       
        if command[0] == 'push': 
            stack.append(int(command[1]))
        elif command[0] == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.popleft())
        elif command[0] == 'size':
            print(len(stack))
        elif command[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif command[0] == 'back':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[len(stack) - 1])
        elif command[0] == 'front':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[0])

    
if __name__ == '__main__':
    solution()
