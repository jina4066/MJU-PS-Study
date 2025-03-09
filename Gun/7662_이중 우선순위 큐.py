import sys, heapq

def solution():     
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        k = int(input())
        minQ, maxQ = [], []
        deleted = [True] * k # 반복문을 도는 인덱스를 ID로 저장
        
        for i in range(k):
            com, n = input().split()
            n = int(n)
            if com == 'I':
                heapq.heappush(minQ, (n, i))
                heapq.heappush(maxQ, (-n, i))
                deleted[i] = False
            else:
                if n == 1:
                    # 삭제되지 않은 값 찾기
                    # 삭제된 값은 힙에서 제거
                    while maxQ and deleted[maxQ[0][1]]:
                        heapq.heappop(maxQ)
                    if maxQ:
                        deleted[maxQ[0][1]] = True
                        heapq.heappop(maxQ)
                else:
                    while minQ and deleted[minQ[0][1]]:
                        heapq.heappop(minQ)
                    if minQ:
                        deleted[minQ[0][1]] = True
                        heapq.heappop(minQ)
    
        while minQ and deleted[minQ[0][1]]:
            heapq.heappop(minQ)
        while maxQ and deleted[maxQ[0][1]]:
            heapq.heappop(maxQ)
        
        if minQ and maxQ:
            print(-maxQ[0][0], minQ[0][0])
        else:
            print('EMPTY')

if __name__ == '__main__':
    solution()

