import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    a = sorted([*map(int, input().split())])
    
    s, e = 0, n - 1
    min_diff = abs(a[0] + a[1])
    ans = (a[0], a[1])
    
    while s < e:
        nums = (a[s], a[e])
        diff = abs(a[s] + a[e])
    
        if min_diff > diff:
            min_diff = diff
            ans = nums
    
        if abs(a[s]) > abs(a[e]):
            s += 1
        elif abs(a[s]) < abs(a[e]):
            e -= 1
        else: # 같으면 바로 출력
            ans = (a[s], a[e])
            break
    
    print(*ans)

if __name__ == '__main__':
    solution()