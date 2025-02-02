import sys

def solution():
    input = sys.stdin.readline
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    psum = sum(a[:x])
    mx, d = psum, 1
    
    for i in range(1, n - x + 1):
        psum = psum - a[i - 1] + a[i + x - 1]
    
        if psum > mx:
            mx = psum
            d = 1
        elif psum == mx:
            d += 1
    
    if mx == 0:
        print("SAD")
    else:
        print(mx)
        print(d)

if __name__ == '__main__':
    solution()
