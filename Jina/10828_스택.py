n = int(input())

stack = []

for _ in range(n):
    oper = input()

    if oper == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
        
    
    elif oper == 'size':
        print(len(stack))
    
    elif oper == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

    elif oper == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    else:
        oper = list(oper.split())
        stack.append(int(oper[1]))
        