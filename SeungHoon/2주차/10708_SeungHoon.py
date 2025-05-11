N = int(input())
M = int(input())

arr = list(map(int,input().split()))
score = [0] * N

for i in range(M):
  ans = list(map(int,input().split()))
  count = 0
  check = arr[i] - 1
  for j in range(N):
    if(arr[i] == ans[j]):
      score[j] += 1
    else:
      count += 1
  score[check] += count
      
for i in range(len(score)):
  print(score[i])
  
# 문제 이해하는데 오래 걸렸다
# 배열이 많아서 헷갈리는데 arr는 각 회차별 타겟을, ans에는 매 게임마다 제출되는 정답을, score에는 득점 결과를 반영했다.
# 처음 반복문 안에서 각 게임마다 제출되는 정답을 입력 받고, 2중 반복문 안에서 제출된 정답이 타겟을 제대로 지정했는지 확인하고
# 일치하면 점수를 추가한다.
# 반대로 불일치하면 타겟에게 추가점수를 주기 위해 count를 1씩 더한다.
# 내부 반복문을 빠져 나온 후 해당 회자의 타겟에게 count(추가점수)를 부여한다.