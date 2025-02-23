import sys
from itertools import combinations

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = []
    nl = [i for i in range(m)]
    
    for _ in range(n):
        a.append(list(map(int, input().split())))

    max_like = 0
    
    for i in combinations(nl, 3):
        like = 0
        for l in a:
            max_v = 0
            for j in list(i):
                v = l[j]
                max_v = max(v, max_v)

            like += max_v
        max_like = max(like, max_like)

    print(max_like)
    
if __name__ == '__main__':
    solution()
