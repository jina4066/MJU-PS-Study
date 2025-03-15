def solution(land):
    # Solution 1
    #for i in range(1, len(land)):
     #   for j in range(len(land[0])):
     #       land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
    
    #return max(land[-1])
    
    # Solution 2
    idxs = set(range(4))
        
    for i in range(1, len(land)):
        for idx in idxs:
            scope = idxs - {idx}
            pre_max_score = 0
            for pre_idx in scope:
                score = land[i - 1][pre_idx]
                if pre_max_score < score:
                    pre_max_score = score
                    
            land[i][idx] += pre_max_score
        
    return max(land[-1])
