def solution(board, h, w):
    answer = 0
    dh, dw = [1, -1, 0, 0], [0, 0, 1, -1]
    color = board[h][w]
    
    for i in range(4):
        x, y = w + dw[i], h + dh[i]
        if x < 0 or y < 0 or x >= len(board) or y >= len(board):
            continue
            
        if board[y][x] == color:
            answer += 1 
            
    return answer