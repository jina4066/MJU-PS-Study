# [BOJ] 나는야 포켓몬 마스터 이다솜 / Silver 4 / 20m
import sys
N,M = map(int,sys.stdin.readline().split())

poketmon = {}
number = {}

for i in range(1, N + 1):
  temp = sys.stdin.readline().strip()
  poketmon[i] = temp
  number[temp] = i

for i in range(M):
  ans = sys.stdin.readline().strip()
  if ans[0].isalpha():
    print(number[ans])
  else:
    print(poketmon[int(ans)])

# 문제가 뒤지게 길다.
# ㅈㄴ 열심히 읽었는데 진짜 문제는 입력에 있었다.
# 입력값으로 포켓몬의 이름이 들어온다
# 딕셔너리를 두개로 나눠
# 하나는 순서를 key로, 하나는 이름을 key로 저장한다.
# 이후 입력값이 문자인지 아닌지를 확인해서
# 문자인 경우 poketmon 딕셔너리에서
# 아닌 경우 number 딕셔너리에서 출력한다.
# 이 문제를 포켓몬 마스터 김영환에게 바칩니다.