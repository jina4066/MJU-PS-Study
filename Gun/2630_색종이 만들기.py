import sys

input = sys.stdin.readline

N = int(input())
a = []

for _ in range(N):
    a.append(list(map(int, input().split())))

w_cnt, b_cnt = 0, 0

def count(s_i, e_i, s_j, e_j):
    global a, w_cnt, b_cnt
    
    n = e_i - s_i + 1    
    w, b = 0, 0

    for i in range(s_i, e_i + 1):
        for j in range(s_j, e_j + 1):
            b += a[i][j]

    w = n ** 2 - b

    if w == n ** 2:
        w_cnt += 1
        
    elif b == n ** 2:
        b_cnt += 1
        
    else:
        n //= 2
        count(s_i, e_i - n, s_j, e_j - n)
        count(s_i, e_i - n, s_j + n, e_j)
        count(s_i + n, e_i, s_j, e_j - n)
        count(s_i + n, e_i, s_j + n, e_j)

count(0, N - 1, 0, N - 1)
print(w_cnt)
print(b_cnt)
