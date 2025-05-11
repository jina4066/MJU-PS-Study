import sys, heapq

def solution():
    input = sys.stdin.readline
    n = int(input())
    q = []
    
    for _ in range(n):
        num = int(input())
        if num == 0:
            if not q:
                print(0)
            else:
                v = heapq.heappop(q)
                if v[1] > 0:
                    print(v[0])
                else:
                    print(-v[0])
        else:
            if num > 0:
                heapq.heappush(q, (num, 1))
            else:
                heapq.heappush(q, (-num, -1))
        
if __name__=='__main__':
    solution()
