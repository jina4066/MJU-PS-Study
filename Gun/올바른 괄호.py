from collections import deque

def solution(s):
    answer = True
    arr = deque(s[0])
    
    for i in range(1, len(s)):
        if s[i] == "(":
            arr.append(s[i])
        else:
            if arr and arr[0] == "(":
                arr.popleft()

    return len(arr) == 0
