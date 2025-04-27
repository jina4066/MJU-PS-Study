from collections import deque

def solution(p, s):
    answer = []
    p = deque(p)
    s = deque(s)
    
    while len(p) > 0:
        for i in range(len(p)):
            p[i] += s[i]

        cnt = 0
        
        while p and p[0] >= 100:
            cnt += 1
            p.popleft()
            s.popleft()
        
        if cnt > 0:
            answer.append(cnt)
    
    return answer
