import sys
import heapq

def solution():
    input = sys.stdin.readline
    n = int(input())
    
    problems = {}  # 문제 번호 -> 난이도
    min_heap = []  # (난이도, 문제 번호) (최소 힙)
    max_heap = []  # (-난이도, -문제 번호) (최대 힙)
    
    for _ in range(n):
        P, L = map(int, input().split())
        problems[P] = L
        heapq.heappush(min_heap, (L, P))
        heapq.heappush(max_heap, (-L, -P))

    m = int(input())

    for _ in range(m):
        command = input().split()

        if command[0] == 'add':
            P, L = int(command[1]), int(command[2])
            problems[P] = L
            heapq.heappush(min_heap, (L, P))
            heapq.heappush(max_heap, (-L, -P))

        elif command[0] == 'solved':
            P = int(command[1])
            if P in problems:
                del problems[P]

        else:  # recommend
            x = int(command[1])
            if x == 1:  # 가장 어려운 문제 추천
                while max_heap and (-max_heap[0][1] not in problems or problems[-max_heap[0][1]] != -max_heap[0][0]):
                    heapq.heappop(max_heap)  # 삭제된 문제 정리
                print(-max_heap[0][1])
            else:  # 가장 쉬운 문제 추천
                while min_heap and (min_heap[0][1] not in problems or problems[min_heap[0][1]] != min_heap[0][0]):
                    heapq.heappop(min_heap)  # 삭제된 문제 정리
                print(min_heap[0][1])

if __name__ == '__main__':
    solution()

