# Sol1
import sys

def solution():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    d = {}
    
    for _ in range(m):
        a, b = sorted(map(int, input().split()))
        
        if a in d.keys():
            d[a].append(b)
        else:
            d[a] = [b]
    
    cnt = 0
    #visited = [False] * n
    
    for i in range(n):
        visited = [False] * n
        
        # d[i]에 포함되는 인덱스 방문 처리
        if i + 1 in d.keys():
            for idx in d[i + 1]:
                visited[idx - 1] = True
        visited[i] = True
    
        # i + 1부터 두 수 탐색하기
        for j in range(i + 1, n):
            if not visited[j]:
                for k in range(j + 1, n):
                    if not visited[k]:
                        if j + 1 in d.keys():
                            if k + 1 in d[j + 1]:
                                continue
                        cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    solution()

# Sol2

import sys

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    d = [set() for _ in range(n + 1)]
    ans = (n * (n - 1) * (n - 2)) // 6
    
    for _ in range(m):
        a, b = map(int, input().split())
        ans -= (n - 2) - len(d[a] | d[b])
        d[a].add(b)
        d[b].add(a)
        
    print(ans)

if __name__ == '__main__':
    solution()
