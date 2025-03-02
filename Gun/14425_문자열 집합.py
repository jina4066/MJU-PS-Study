import sys

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = set()
    cnt = 0
    
    for _ in range(n):
        a.add(input().strip()) 

    for _ in range(m):
        b = input().strip()
        if b in a:
            cnt += 1

    print(cnt)


if __name__=='__main__':
    solution()
