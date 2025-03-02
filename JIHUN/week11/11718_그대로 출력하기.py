import sys

for line in sys.stdin:  # EOF(입력 종료)까지 한 줄씩 읽음
    print(line, end="")  # 입력 그대로 출력 (줄바꿈 유지)

#모두 새로 알게 된 내용. sys.stdin은 입력 종료를 자동으로 감지, 줄바꿈 유지를 위해 line, end="" 사용