N, M = map(int, input().split())  # 보드 크기 입력
original = []   # 보드 리스트
count = []   # 다시 칠해야 하는 최소 개수 저장 리스트

# 보드 내용 저장
for _ in range(N):
    original.append(input())

# a, b는 보드 시작점 좌표
for a in range(N-7):
    for b in range(M-7):
        index1 = 0   # 왼쪽 위를 흰색(W)로 바꿀 때 필요한 칸 수
        index2 = 0   # 왼쪽 위를 검은색(B)로 바꿀 때 필요한 칸 수

        # 8x8 보드 탐색
        for i in range(a, a+8):
            for j in range(b, b+8):
                # 좌표합이 짝수라면 왼쪽 위의 색과 동일해야 함, 홀수라면 왼쪽 위와 반대여야 함
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        # 최소 색칠해야 하는 개수 저장
        count.append(min(index1, index2))

print(min(count))

# N-7과 M-7은 8x8 크기의 체스판의 시작점 범위를 설정하기 위해 사용됨
# 브루트포스로 가능한 모든 8x8 크기의 체스판을 확인함