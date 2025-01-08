import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

# solution 1: Library

for i in permutations(a, m):
    print(*list(i))

# solution 2: Backtracking

visited = [False for _ in range(n)]

def dfs(depth):    
    if depth == m:
        print(' '.join(out))
        return
        
    for i in range(n): 
        if not visited[i]:
            visited[i] = True
            out.append(str(a[i]))
            dfs(depth + 1)
            out.pop()
            visited[i] = False

out = []
dfs(0)