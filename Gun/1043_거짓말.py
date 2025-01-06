import sys
input = sys.stdin.readline

n, m = map(int, input().split())
true = set(list(map(int, input().split()))[1:])
parties = []

for _ in range(m):
    people = set(list(map(int, input().split()))[1:])
    parties.append(people)

# 진실을 아는 사람들이 속한 파티부터 방문
for _ in range(m):  
    for party in parties:
        if len(party & true) > 0:
            true = true.union(party)
             
# true에 속하지 않는 파티 개수 세기
count = 0

for party in parties:
    if len(party & true) == 0:
        count += 1
            
print(count)
