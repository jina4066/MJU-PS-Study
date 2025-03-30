def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:
            i -= 1
            break
    return i + 1

# pop을 이용한 풀이

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
