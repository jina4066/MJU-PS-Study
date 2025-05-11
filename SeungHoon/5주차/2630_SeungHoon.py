# 색종이 만들기 / Silver 2 / 1h 30m
N = int(input())

arr = []
ans = [0, 0]

for i in range(N):
  line = list(map(int,input().split()))
  arr.append(line)
  
def origami(x, y, N):
  color = arr[x][y]
  for i in range(x, x+N):
    for j in range(y, y+N):
      if color != arr[i][j]:
        origami(x,y,N//2)
        origami(x,y+N//2,N//2)
        origami(x+N//2,y,N//2)
        origami(x+N//2,y+N//2,N//2)
        return
  if(color == 0):
    ans[0] += 1
  else:
    ans[1] += 1

origami(0,0,N)

for i in range(len(ans)):
  print(ans[i])

# 분할 정복으로 푸는 문제
# 최초에 0,0에서 시작해서 조건을 충족하지 못하면
# 테이블을 4개의 사분면으로 나누고
# 다시 탐색을 시작한다.
# 이를 재귀 함수로 구현한다.