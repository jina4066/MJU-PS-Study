import sys
input = sys.stdin.readline

# n: 포켓몬 개수, m: 문제 개수
n, m = map(int, input().split())

poketmon_num_to_name = {}  # {번호: 이름}
poketmon_name_to_num = {}  # {이름: 번호}

for i in range(1, n + 1):
    name = input().strip()
    poketmon_num_to_name[i] = name  # 숫자 → 이름 매핑
    poketmon_name_to_num[name] = i  # 이름 → 숫자 매핑

for _ in range(m):
    question = input().strip()
    if question.isdigit():  # 숫자로 질문한 경우, 이름 출력
        print(poketmon_num_to_name[int(question)])
    else:  # 이름으로 질문한 경우, 번호 출력
        print(poketmon_name_to_num[question])
