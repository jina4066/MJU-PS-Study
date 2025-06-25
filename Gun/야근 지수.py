import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    q = [-work for work in works]
    heapq.heapify(q)
    
    for _ in range(n):
        max_work = -heapq.heappop(q)
        heapq.heappush(q, -(max_work - 1))
    
    return sum(w ** 2 for w in q)
