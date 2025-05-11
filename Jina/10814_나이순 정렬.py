import sys
input = sys.stdin.readline

n = int(input())
people = []

for _ in range(n):
    age, name = input().split()
    people.append([int(age), name])

for i in sorted(people, key=lambda x : x[0]):
    print(i[0], i[1])

# 나이가 같다면 가입순으로 정렬하는 것을 어떻게 구현할지 고민했는데,
# 애초에 리스트는 입력된 순서로 정렬되므로, 나이가 동일한 경우 원래 가입순서가 유지된다