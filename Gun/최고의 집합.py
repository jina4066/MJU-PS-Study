def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    
    for divisor in range(n, 0, -1):
        v = s // divisor
        answer.append(v)
        s -= v
    
    return answer