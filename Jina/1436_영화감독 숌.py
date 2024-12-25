N = int(input())
cnt = 0   # 종말의 숫자 찾은 개수
result = 666  # 첫번째 종말의 숫자

while True:
    if '666' in str(result):
        cnt += 1

    if cnt == N:
        break

    result += 1

print(result)

# 브루트포스 문제로 666이 포함되는걸 n이 될때까지 반복하고 break