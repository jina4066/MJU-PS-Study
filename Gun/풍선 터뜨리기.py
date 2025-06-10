def solution(a):
    answer = 0
    n = len(a)
    left_min = [0] * n
    right_min = [0] * n

    min_val = a[0]    
    for i in range(n):
        min_val = min(min_val, a[i])
        left_min[i] = min_val
        
    min_val = a[-1]
    for i in range(n - 1, -1, -1):
        min_val = min(min_val, a[i])
        right_min[i] = min_val
        
    for i in range(n):
        if a[i] > left_min[i] and a[i] > right_min[i]:
            continue
        else:
            answer += 1
            
    return answer