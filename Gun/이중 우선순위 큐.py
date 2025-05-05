import heapq

def solution(operations):
    deleted = [False] * len(operations)
    min_heap = []
    max_heap = []
    
    for idx, operation in enumerate(operations):
        command, number = operation.split()
        if command == 'I':
            heapq.heappush(min_heap, (int(number), idx))
            heapq.heappush(max_heap, (-int(number), idx))
            
        elif command == 'D':
            if number == '-1':
                while min_heap and deleted[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    deleted[min_heap[0][1]] = True
                    heapq.heappop(min_heap)
            else:
                while max_heap and deleted[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    deleted[max_heap[0][1]] = True
                    heapq.heappop(max_heap)
                    
    while min_heap and deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    while max_heap and deleted[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    answer = []
    
    if not min_heap or not max_heap:
        answer = [0, 0]
    else:
        answer = [-max_heap[0][0], min_heap[0][0]]
    
    return answer
