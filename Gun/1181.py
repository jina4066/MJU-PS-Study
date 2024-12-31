import sys
input = sys.stdin.readline

n = int(input())
# 중복 제거를 위해 set 자료구조 사용
a = set()

for _ in range(n):
    # rstrip 메서드를 통해 공백은 입력받지 않게 함
    a.add(input().rstrip())

d = list(a)
# 단어 길이를 우선 순위로 정렬하기 위해 람다 정렬 사용
# set 자료구조로는 불가하므로 list로 변경
for word in sorted(d, key=lambda x: [len(x), x]):
    print(word)
