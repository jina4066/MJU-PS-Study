// Sol 1.
from collections import deque

def solution(p, loc):
    p = deque(p)
    l = len(p)
    a = [0] * l
    idx = 0
    rank = 1

    while len(p) > 0:
        process = p.popleft()
        
        if p and process < max(p):
            p.append(process)
        else:
            if idx == loc:
                return rank
            a[idx] = rank
            rank += 1
        
        idx = (idx + 1) % l
        
        while a[idx] > 0:
            idx = (idx + 1) % l
            
    return a[loc]

// Sol 2.
from collections import deque

def solution(priorities, location):
    queue = deque([(priority, i) for i, priority in enumerate(priorities)])
    rank = 1

    while queue:
        cur, idx = queue.popleft()
        
        # 중요도가 더 높은 게 남아있으면 다시 넣음
        if any(cur < other[0] for other in queue):
            queue.append((cur, idx))
        else:
            if idx == location:
                return rank
            rank += 1
