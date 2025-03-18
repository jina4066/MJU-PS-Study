while True:
    try:
        a, b = map(int, input().split())
        if a == 0 and b == 0:  # 종료 조건 수정
            break
        else:
            print(a + b)
    except EOFError:
        break