# [BOJ] 부녀회장이 될테야 / Bronze 1 / 30m
T = int(input())
for i in range(T):
  k = int(input())
  n = int(input())
  arr = [j for j in range(1, n+1)]

  for x in range(k):
    arr2 = []
    for y in range(n):
      arr2.append(sum(arr[:y+1]))
    arr = arr2.copy()
  
  print(arr[-1])

# 0층의 사람들을 리스트에 입력한다.
# k(층수)만큼 반복하고, n(호수)만큼 2중 반복한다.
# 새로운 리스트에 각 호수별로 아래층의 1~n호까지의 합을 넣는다
# 이를 원래 리스트에 복사한다
# arr[-1]을 출력해 입력받은 k층 n호에 사는 인원수를 출력한다.