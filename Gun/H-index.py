def solution(citations):
    answer = 0
    citations.sort()

    for h_idx in range(len(citations) + 1):
        h_cnt = 0
        
        for citation in citations:
            if citation >= h_idx:
                h_cnt += 1
            if h_idx < h_cnt:
                break        
        
        if h_idx > h_cnt:
            break
        answer = h_idx
            
    return answer
