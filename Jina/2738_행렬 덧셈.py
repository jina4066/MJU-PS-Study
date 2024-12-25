A, B = [], []  # 행렬 입력 받을 리스트 A, B 선언

N, M = map(int, input().split())  # 행렬 크기 입력

# 행렬 원소 입력
for row in range(N): 
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N): 
    row = list(map(int, input().split()))
    B.append(row)

# 행렬 덧셈 후 출력
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')

    print()

# 2차원 리스트를 사용하여 행렬 저장 및 연산