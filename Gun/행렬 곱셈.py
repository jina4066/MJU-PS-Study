def multiple(arr1, arr2):
    size = len(arr1)
    answer = 0
    
    for i in range(size):
        answer += arr1[i] * arr2[i]
    
    return answer

def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    # change the arr2's col and row
    new = [[0] * len(arr2) for _ in range(len(arr2[0]))]
    
    for col in range(len(arr2)):
        for row in range(len(arr2[0])):
            new[row][col] = arr2[col][row]
    
    for col in range(len(arr1)):
        for row in range(len(arr2[0])):
            answer[col][row] = multiple(arr1[col], new[row])
            
    return answer

# Sol2.
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
