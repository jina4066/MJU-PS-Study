import sys

def solution():     
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # 누적 합 구하기
    for i in range(1, n):
        a[i] += a[i - 1]
    
    # 정렬 후 k번째까지 합 구하기
    print(sum(sorted(a)[-k:]))

if __name__== '__main__':
    solution()
