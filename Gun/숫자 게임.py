def solution(A, B):
    answer, a = 0, 0
    A.sort()
    B.sort()
    for b in range(len(B)):
        if A[a] < B[b]:
            answer += 1
            a += 1
            
    return answer