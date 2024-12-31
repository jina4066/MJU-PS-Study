t = int(input())

for _ in range(t):
    n = int(input())
    # a: 0이 출력되는 횟수, b: 1이 출력되는 횟수 
    a, b = 1, 0
    
    for _ in range(n):
        # python 언어의 특성상 변수들을 swap할 때 temp 변수를 직접 사용하지 않아도 됨
        a, b = b, a + b
    
    print(a, b)