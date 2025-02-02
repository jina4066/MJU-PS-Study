import sys
input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    oper = input().split()

    if oper[0] == 'push':
        queue.append(oper[1])

    elif oper[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)

    elif oper[0] == 'size':
        print(len(queue))
    
    elif oper[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif oper[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif oper[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)