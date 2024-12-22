9465. 스티커

import sys
input = sys.stdin.readline

# 완전 탐색으로도 풀 수 있지만, 시간 복잡도를 고려해 DP로 풀어야 함
# i번커에 뜯을 스티커를 찾으려면 i - 1번째에 뜯은 스티커와 다른 행의 스티커를 뜯거나,
# i - 2번째에 마지막으로 뜯은 스티커(행 상관없음)가 있으면 된다.
# 따라서 i >= 2일 때, (1 or 2)층 i번째 자리의 최고 점수는 
# max((2 or 1)층 i - 1번째 최고 점수, i - 2 번째 자리의 최고 점수 중 큰 점수) 라는 점화식을 세울 수 있다.

t = int(input())

for _ in range(t):
    n = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))

    # n = 1일 때 IndexError를 방지하기 위해 조건문을 추가했다.
    if n == 1: 
        print(max(a1[0], a2[0]))
        continue
        
    a1[1], a2[1] = a1[1] + a2[0], a2[1] + a1[0]

    for i in range(2, n):
        a1[i] += max(a2[i - 1], max(a1[i - 2], a2[i - 2]))
        a2[i] += max(a1[i - 1], max(a1[i - 2], a2[i - 2]))

    print(max(a1[n - 1], a2[n - 1]))
