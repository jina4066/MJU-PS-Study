import sys
sys.setrecursionlimit(10**6)

def solution(arr):
    zero, one = 0, 0
    l = len(arr)
    
    def divide(row_case, col_case):
        nonlocal zero, one
        row_s, row_e = row_case
        col_s, col_e = col_case        
        n = row_e - row_s
        if n <= 1:
            if arr[row_s][col_s] == 0:
                zero += 1
            else:
                one += 1
            return
    
        cnt = 0
        for row in range(row_s, row_e):
            for col in range(col_s, col_e):
                cnt += arr[row][col]

        # every number is '0' or '1'
        if cnt == n ** 2:
            one += 1
            return 
        elif cnt == 0:
            zero += 1
            return
        
        divide((row_s, row_s + n//2), (col_s, col_s + n//2))
        divide((row_s, row_s + n//2), (col_s + n//2, col_e))
        divide((row_s + n//2, row_e), (col_s, col_s + n//2))
        divide((row_s + n//2, row_e), (col_s + n//2, col_e))  

    divide((0, l), (0, l))

    return zero, one