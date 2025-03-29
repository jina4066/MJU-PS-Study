# [BOJ] FizzBuzz / Bronze 1 / 20m
for i in range(3, 0, -1):
    temp = input()
    if temp not in ["Fizz", "Buzz", "FizzBuzz"]:
        n = int(temp) + i
if not n % 3 and not n % 5:
    print("FizzBuzz")
elif not n % 3 and n % 5:
    print("Fizz")
elif n % 3 and not n % 5:
    print("Buzz")
else:
    print(n)

# 연속된 3개의 문자열을 입력 받는다
# 입력받은 문자열이 Fizz,Buzz,FizzBuzz가 아니라 숫자이면서
# 첫번째 값이면 + 3, 두번째 값이면 + 2, 세번째 값이면 + 1을 해준다.
# 이후 출력은 조건에 따라 if, else로 구현한다.