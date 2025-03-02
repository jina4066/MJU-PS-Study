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
                print(-heapq.heappop(q))
        else:
            heapq.heappush(q, -num)
        
if __name__=='__main__': 
    solution()
