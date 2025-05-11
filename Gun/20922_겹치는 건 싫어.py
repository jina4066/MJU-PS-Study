import sys

def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    v = [0] * (2 * 100_000 + 1)
    
    s, e, ans = 0, 0, 0
    
    while e < n:
        num = a[e]
        v[num] += 1
        
        if v[num] > k:        
            ans = max(ans, e - s)
    
            while v[num] > k:
                v[a[s]] -= 1
                s += 1
                
        e += 1
    
    ans = max(ans, e - s)
    print(ans)
    
if __name__ == '__main__':
    solution()
