while True:
    N = int(input())

    if N == -1:      # N이 -1이면 종료
        break

    num_list = []

    # i가 N의 약수라면 리스트에 추가
    for i in range(1, N):   # N-1까지만 반복문을 돌려 N은 포함되지 않도록 함
        if N % i == 0:    
            num_list.append(i)
    
    if sum(num_list) == N:
        print(N, " = ", " + ".join(str(i) for i in num_list), sep="")
    else:
        print(N, 'is NOT perfect.')
    