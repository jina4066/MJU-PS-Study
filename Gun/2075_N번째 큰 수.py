import sys, heapq

def solution():
    input = sys.stdin.readline
    n = int(input())
    q = []

    for _ in range(n):
        a = list(map(int, input().split()))
        if not q:
            for v in a:
                heapq.heappush(q, v)
        else:
            for v in a:
                if q[0] < v:
                    heapq.heappush(q, v)
                    heapq.heappop(q)
    print(q[0])
            

if __name__=='__main__':
    solution()
