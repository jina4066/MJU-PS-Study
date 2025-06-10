def solution(cookie):
    answer = 0
    # 1 ~ l  l ~ r  r ~ m  m ~ n
    # sum(l ~ r) == sum(r ~ m) 인지?
    # 3 pointers -> l, r, m
    # r이 움직이면서 l, m 확장
    for i in range(len(cookie) - 1): # 중간 포인터 r
        left = i
        right = i + 1
        lsum = cookie[left]
        rsum = cookie[right]
        
        while True:
            if lsum == rsum:
                answer = max(answer, lsum)
                
            if left > 0 and lsum <= rsum:
                left -= 1
                lsum += cookie[left]
            elif right < len(cookie) - 1 and lsum >= rsum:
                right += 1
                rsum += cookie[right]
                
    return answer