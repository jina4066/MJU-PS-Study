import sys
from collections import Counter

def solution():
    input = sys.stdin.readline
    n = int(input())
    c = []

    for _ in range(n):
        a, b = input().split(".")
        c.append(b.strip())

    d = Counter(c)
    
    for key in sorted(d.keys()):
        print(key, d[key])
    
if __name__ == '__main__':
    solution()