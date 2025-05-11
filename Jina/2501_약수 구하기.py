N, K = map(int, input().split())
num_list = []

for i in range(1, N+1):    # N의 약수 개수 모두 구하기
    if N % i == 0:
        num_list.append(i)

        if len(num_list) == K:     # 현재 리스트에 추가된 약수의 개수가 K와 같으면 값 출력
            print(num_list[K-1])
            break

        i += 1

if len(num_list) < K:    # 리스트 원소의 개수가 K보다 작으면 0 출력
    print(0)
