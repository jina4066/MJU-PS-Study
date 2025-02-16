import sys
from itertools import permutations

def solution():
    input = sys.stdin.readline
    n = int(input())
    k = int(input())
    a = []
    
    for _ in range(n):
        a.append(int(input()))
    
    s = set()
    
    for i in permutations(a, k):
        number = ""
        for v in list(i):
            number += str(v)
        s.add(number)
            
    print(len(s))

if __name__ == '__main__':
    solution()
