import heapq

def solution(k, score):
    answer = []
    board = []
    for s in score:
        heapq.heappush(board, s)
        if len(board) > k:
            heapq.heappop(board)
        answer.append(board[0])
    return answer
