import math

def solution(n, stations, w):
    answer = 0
    bad_spots = []
    idx = 1
    divider = w * 2 + 1
    
    for s in stations:
        if idx <= s - w:
            answer += math.ceil((s - w - idx) / divider)
        
        idx = s + w + 1
    
    answer += math.ceil((n + 1 - idx) / divider)

    return answer
