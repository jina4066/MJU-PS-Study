import sys

def solution():
    input = sys.stdin.readline

    while v := input():
        a, b = map(str, v.split())
        idx = 0
    
        for i in range(len(b)):
            if a[idx] == b[i]:
                idx += 1
            if idx >= len(a):
                break
    
        if idx >= len(a):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solution()