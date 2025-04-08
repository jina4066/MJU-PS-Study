# [BOJ] 패션왕 신해빈 / Silver 3 / 40m
T = int(input())

for i in range(T):
  arr = {}
  N = int(input())
  for j in range(N):
    name, wears = map(str,input().split())
    if wears in arr:
      arr[wears].append(name)
    else:
      arr[wears] = [name]
    
  count = 1

  for k in arr:
    count *= (len(arr[k]) + 1)
  
  print(count - 1)

# 딕셔너리를 이용해서 푸는 문제
# 먼저 의상의 종류를 key,의상의 이름을 value로 해서 딕셔너리에 저장한다.
# 각 종류에서 선택할 수 있는 경우의 수는
# 입는 경우 + 안입는 경우(1)이므로
# 의상의 종류만큼 이를 곱해 준 후
# 모든 종류에서 안입는 경우를 제거하기 위해
# 1을 빼서 출력한다.
