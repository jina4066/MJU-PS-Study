import sys
from collections import Counter

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    a = [[] for _ in range(m)]

    for _ in range(n):
        s = input().strip()
        for i in range(m):
            a[i].append(s[i])

    alphabet = ""
    hd = 0
    
    for s in a:
        c = Counter(s)
        max_cnt = max(list(c.values()))
        s = []
        for key in c.keys():
            if c[key] == max_cnt:
                s.append(key)
    
        alphabet += sorted(s)[0]
        hd += n - max_cnt

    print(alphabet)
    print(hd)
            
if __name__ == '__main__':
    solution()
