import sys
input = sys.stdin.readline

# 입력값을 num으로 하는 변수를 선언하기 위해 ()와 := 연산자 활용
while (num := int(input())) != 0:
    s = str(num)
    # 문자열, 리스트를 뒤집을 때 [::-1] 사용 
    if s == s[::-1]:
        print("yes")
    else:
        print("no")