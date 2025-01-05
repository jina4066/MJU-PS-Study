N = int(input())
fact = 1

for i in range(2, N+1):
    fact *= i

str_fact = str(fact)

cnt = 0

for i in range(len(str(fact))):
    if str_fact[-1 - i] != '0':  # 끝에서부터 i번째 위치의 문자가 0이 아니라면 break
        break
    cnt += 1

print(cnt)

